---
type: blog
date: "2021-12-13T15:51:45Z"
author: Jonny Spicer
title: "Advent of Code V"
categories:
- Programming
series: ["Advent of Code"]
---
These next three problems started out not too badly for me, but then got progressively harder. Day 12 in particular really
highlighted my lack of computer science background and knowledge of well-known algorithms - I knew that I needed to implement
a variation on a depth-first search algorithm, but doing so correctly still took me several hours. Trying to build the mental
model for recursively traversing the graph was a real struggle, but one which I hope will be worth it in the future.

## Day 10

Today's problem was a classic bracket matcher. Lines are "corrupt" if the wrong corresponding bracket is found in the string, or may
simply be incomplete. Part one required a score to be calculated from all the corrupt lines, with the first illegal character in each string
being worth a certain amount. Part two examined the incomplete lines, and required a score to be generated based off which characters were
required to complete them, before finding the middle value for the scores of all the lines. Given that I have seen this kind of problem
before and knew already that stacks are a good option, I didn't find this one too bad at all.

```html
Example input:
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
```

```go
type stack []rune

func Ten(input []string) (int, int) {
	sum := 0

	// needed for part 2
	var incompleteStacks []stack

	for _, row := range input {
		// a placeholder char so we can see if our row is corrupted
		foundInstead := '?'
		s := stack{}

		for _, char := range row {
			if foundInstead != '?' { break }

			lc := s.peek()

			switch char {
			case '(','[', '{', '<':
				s.push(char)
			case ')':
				if lc == '(' {
					s = s.pop()
				} else {
					foundInstead = char
				}
			case ']':
				if lc == '[' {
					s = s.pop()
				} else {
					foundInstead = char
				}
			case '}':
				if lc == '{' {
					s = s.pop()
				} else {
					foundInstead = char
				}
			case '>':
				if lc == '<' {
					s = s.pop()
				} else {
					foundInstead = char
				}
			}

			switch foundInstead {
			case ')':
				sum += 3
			case ']':
				sum += 57
			case '}':
				sum += 1197
			case '>':
				sum += 25137
			}
		}

		// if the row isn't corrupted and has unmatched runes
		if foundInstead == '?' && len(s) > 0 {
			incompleteStacks = append(incompleteStacks, s)
		}
	}

	var scores []int

	for _, s := range incompleteStacks {
		score := 0
		// traverse the stack of unmatched runes from right to left
		for i := len(s) - 1; i >= 0; i-- {
			score *= 5
			switch s[i] {
			case '(':
				score += 1
			case '[':
				score += 2
			case '{':
				score += 3
			case '<':
				score += 4
			}
		}

		scores = append(scores, score)
	}

	sort.Ints(scores)

	return sum, scores[len(scores)/2]
}

func (s *stack) push(char rune) {
	*s = append(*s, char)
}

// couldn't figure out a way to make this work with
// a pointer to the original stack :(
func (s stack) pop() stack {
	return s[:len(s)-1]
}

func (s stack) peek() rune {
	if len(s) > 0 {
		return s[len(s)-1]
	}
	// a placeholder char as I couldn't be bothered to
	// mess around with nil pointer references
	return '0'
}
```

## Day 11

This problem involved a grid of counters, each of which would increment with every step, and if any individual value reached 10, would also
increment all adjacent counters in the grid before being reset to 0. The first step required you to calculate the total number of times
counters reached 10 after 100 steps, and the second to work out the first number of steps on which all the counters would read 10.

```html
Example input:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```

```go
type octopus int
type coord struct {
	x, y int
}

func Eleven(input []string) (int, int) {
	octoGrid := map[int][]octopus{}
	for y, row := range input {
		rs := []rune(row)
		for _, r := range rs {
			if r == '\r' { continue }
			octoGrid[y] = append(octoGrid[y], octopus(int(r) - '0'))
		}
	}

	flashes := 0
	firstAllFlash := 0

	for i := 0; i < 10000; i++ {
		for y, row := range octoGrid {
			for x, octo := range row {
				octoGrid[y][x] = octo.step(coord{x, y}, octoGrid)
			}
		}

		allFlash := true

		for y, row := range octoGrid {
			for x, octo := range row {
				if octo == 10 {
					flashes++
					octoGrid[y][x] = 0
				} else {
					allFlash = false
				}
			}
		}

		if allFlash {
			firstAllFlash = i
			break
		}
	}

	return flashes,firstAllFlash
}

func (o octopus) step(c coord, octoGrid map[int][]octopus) octopus {
	if o == 10 { return o }
	octoGrid[c.y][c.x] += 1
	if octoGrid[c.y][c.x] == 10 {
		ao := getAdjacentOctopi(octoGrid, c)
		for _, co := range ao {
			octoGrid[co.y][co.x] = octoGrid[co.y][co.x].step(co, octoGrid)
		}
	}

	return octoGrid[c.y][c.x]
}

func getAdjacentOctopi(m map[int][]octopus, c coord) []coord {
	adj := []coord{}

	if c.y-1 >= 0 {
		adj = append(adj, coord{c.x, c.y-1}) // top
		if c.x-1 >= 0 {
			adj = append(adj, coord{c.x-1, c.y-1}) // top left
		}
		if c.x+1 < len(m[0]) {
			adj = append(adj, coord{c.x+1, c.y-1}) // top right
		}
	}

	if c.x-1 >= 0 {
		adj = append(adj, coord{c.x-1, c.y}) // left
	}
	if c.x+1 < len(m[0]) {
		adj = append(adj, coord{c.x+1, c.y}) // right
	}

	if c.y+1 < len(m) {
		adj = append(adj, coord{c.x, c.y+1}) // bottom
		if c.x-1 >= 0 {
			adj = append(adj, coord{c.x-1, c.y+1}) // bottom left
		}
		if c.x+1 < len(m[0]) {
			adj = append(adj, coord{c.x+1, c.y+1}) // bottom right
		}
	}

	return adj
}
```

## Day 12

I struggled with day 12 a lot, as described in the intro. I'm not familiar with working with graphs at all, or particularly with recursion
for that matter, which made this one a real challenge. I spent about three hours on it on Sunday morning, had no luck, went out for my usual
long run and then spent another couple of hours on it on my return before cracking it. My brain hurt throughout.

```html
Example input:
start-A
start-b
A-c
A-b
b-d
A-end
b-end
```

```go
func Twelve(input []string) (int, int) {
	caves := map[string]*node{}

	for _, row := range input {
		lr := strings.Split(row, "-")
		l, r := lr[0], strings.TrimSuffix(lr[1], "\r")

		if _, ok := caves[l]; ok {
			// if entry for cave exists in map, update it
			caves[l].vertices = append(caves[l].vertices, r)
		} else {
			caves[l] = &node{
				name:     l,
				vertices: []string{r},
				big:      unicode.IsUpper(rune(l[0])),
			}
		}

		if _, ok := caves[r]; ok {
			// if entry for cave exists in map, update it
			caves[r].vertices = append(caves[r].vertices, l)
		} else {
			caves[r] = &node{
				name:     r,
				vertices: []string{l},
				big:      unicode.IsUpper(rune(r[0])),
			}
		}
	}

	return twelve(caves, true),twelve(caves, false)
}

func twelve(caves map[string]*node, part1 bool) int{
    // these four variables should be extracted into some kind of state
    // but I was just so happy it worked I couldn't be bothered to refactor :)
	var currentPath []string
	visited := map[string]struct{}{}
	count := 0
	repeatedCave := ""

	traverse(*caves["start"], visited, currentPath, &count, caves, false, &repeatedCave, part1)

	return count
}

type node struct {
	name string
	vertices []string
	big bool
}

func traverse(
	n node,
	visited map[string]struct{},
	currentPath []string,
	count *int,
	caves map[string]*node,
	doubleCaved bool,
	repeatedCave *string,
	part1 bool,
	) {
	// we can't go back to the start twice
	if  n.name == "start" && len(visited) > 0 {
		return
	}

	if _, ok := visited[n.name]; ok {
		// can't go back to a small cave in part 1
		// can't go back to more than one small cave in part 2
		if doubleCaved || part1  { return }
		doubleCaved = true
		*repeatedCave = n.name
	} else if !n.big { visited[n.name] = struct{}{} }

	currentPath = append(currentPath, n.name)

	if n.name == "end" {
		*count++
		delete(visited, n.name)
		currentPath = currentPath[:len(currentPath)-1]
		return
	}

	for _, vertex := range n.vertices {
		traverse(*caves[vertex], visited, currentPath, count, caves, doubleCaved, repeatedCave, part1)
	}

	currentPath = currentPath[:len(currentPath)-1]

	if n.name == *repeatedCave {
		*repeatedCave = ""
		doubleCaved = false
	} else {
		delete(visited, n.name)
	}
}
```