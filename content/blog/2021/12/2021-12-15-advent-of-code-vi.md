---
type: blog
date: "2021-12-15T19:02:35Z"
author: Jonny Spicer
title: "Advent of Code VI"
categories:
- Programming
series: ["Advent of Code"]
---
Another three days, another three challenges. I must admit, I am definitely starting to reach my limit with these; day 13 felt very
manageable but on day 14 I completely failed to learn from mistakes on previous days, and my solution to day 15 is just heinous... it
takes circa 90 minutes on my fairly beefy machine to generate the correct answer. But, much like you *have* heard of Captain Jack
Sparrow, it *does* produce the right answer.

## Day 13
Today's problem was a relatively gentle one. Presented with a series of points on a grid and a set of instructions to fold said grid
along certain planes, first find the total number of points after the first fold, and then find what capital letters the points on the
grid spell out after all folds are completed. I thought part two was pretty amusing, given that it didn't really require any changes to
the logic from part 1, it was just a bit of fiddling around to get my data structure to print out.

```html
Example input:
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
```

```go
func Thirteen(input []string) (int, int) {
	return thirteen(input, true), thirteen(input, false)
}

func thirteen(input []string, part1 bool) int {
	grid := map[int]map[int]bool{}

	for _, row := range input {
		// v lazy way of checking if it's a blank line
		if len(row) < 2 { continue }

		if row[0] == 'f' {
			// parse instruction
			row = strings.TrimPrefix(row, "fold along ")
			lineNumber := utils.ExtractInts(row)[0]
			if row[0] == 'x' {
				// iterate over grid
				for y, _ := range grid {
					for x, _ := range grid[y] {
						if x >= lineNumber {
							// add the missing values
							grid[y][lineNumber - (x - lineNumber)] = true
						}
					}
				}

				// remove the lines that we've folded over
				for y, _ := range grid {
					for x, _ := range grid[y] {
						if x >= lineNumber {
							delete(grid[y], x)
						}
					}
				}
			}

			if row[0] == 'y' {
				// iterate over grid
				for y, _ := range grid {
					if y >= lineNumber {
						currLine := lineNumber - (y - lineNumber)
						for x, _ := range grid[y] {
							// if the row doesn't exist in the grid (ie its empty)
							if _, ok := grid[currLine]; !ok {
								// add it
								grid[currLine] = map[int]bool{}
							}
							if _, ok := grid[currLine][x]; !ok {
								grid[currLine][x] = true
							}
						}
					}
				}

				for y, _ := range grid {
					if y >= lineNumber {
						delete(grid, y)
					}
				}
			}

			if part1 {
				break
			}
		} else {
			xy := utils.ExtractInts(row)
			// if the y value already existed in the grid
			if _, ok := grid[xy[1]]; ok {
				// add the x value to it
				grid[xy[1]][xy[0]] = true
			} else {
				// else create the y and add the x as its first value
				grid[xy[1]] = map[int]bool{xy[0]:true}
			}
		}
	}

	count := 0

	var keys []int
	for key, _ := range grid {
		keys = append(keys, key)
	}
	sort.Ints(keys)

	for i := 0; i <= keys[len(keys)-1]; i++ {
		if _, ok := grid[i]; ok {
			count += len(grid[i])
		}
		if !part1{
			printRow(grid[i])
		}
	}

	return count
}

func printRow(row map[int]bool) {
	var keys []int
	for key, _ := range row {
		keys = append(keys, key)
	}
	sort.Ints(keys)

	for i := 0; i < keys[len(keys)-1]; i++ {
		if _, ok := row[i]; ok {
			fmt.Printf("#")
		} else {
			fmt.Printf(".")
		}
	}
	fmt.Printf("\n")
}
```

## Day 14
This one made a total fool of me. Way back on [day 6](/blog/advent-of-code-iii) the problem involved modeling a population, and you may
remember that I naively held an object for each member of the population in memory, before coming to the stark realisation that my PC has
nowhere near enough RAM to make up for that kind of abysmal solution. I, however, did *not* remember this, and instead chose to do exactly
the same thing for today's very similar problem, and again I have included my naive solution. The challenge is, given a string and a list
of insertion rules, to work out how many of each letter will be in the string after a certain number of rounds of insertion, and then
find the difference between the most common and least common letters. The trap is, of course, to try to compute the whole string at every
stage.

```html
Example input:
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
```

```go
func Fourteen(input []string) (int, int) {
	return fourteen(input, 10), fourteen(input, 40)
}

func fourteen(input []string, iterations int) int {
	polymer := strings.TrimSpace(input[0])
	mappings := map[string][]string{}
	pairs := map[string]int{}
	letters := map[rune]int{}

	for i := 2; i < len(input); i++ {
		mapping := strings.Split(input[i], " -> ")
		// for each pair, store the two other pairs it will create after the insertion
		mappings[mapping[0]] = []string{
			mapping[0][:1] + strings.TrimSpace(mapping[1]),
			strings.TrimSpace(mapping[1]) + mapping[0][1:],
		}

		// Add a new entry in the pairs map
		pairs[mapping[0]] = 0
	}

	// store the letters from the initial polymer string
	for _, char := range polymer {
		if _, ok := letters[char]; !ok {
			letters[char] = 1
		} else {
			letters[char]++
		}
	}

	// store the initial pairs
	for j := 0; j < len(polymer) - 1; j++ {
		key := string(polymer[j]) + string(polymer[j+1])
		pairs[key]++
	}

	for i := 0; i < iterations; i++ {
		temp := map[string]int{}

		// for every pair
		for pair, pairCount := range pairs {
			if pairCount == 0 { continue }

			// the pairs we'll need to update
			toUpdate := mappings[pair]

			// add the appropriate number of newly created letters
			letters[rune(toUpdate[0][1])] += pairCount

			// store number of extra pairs created in temp map
			for key := range toUpdate {
				if _, ok := temp[toUpdate[key]]; !ok {
					temp[toUpdate[key]] = pairCount
				} else {
					temp[toUpdate[key]] += pairCount
				}
			}
		}

		// copy the values from the temp map into the main one
		for key := range pairs {
			if _, ok := temp[key]; ok {
				pairs[key] = temp[key]
			} else {
				// if there is no value in the temp map, set the main one to 0
				pairs[key] = 0
			}
		}
	}

	var vals []int

	for _, val := range letters {
		vals = append(vals, val)
	}

	sort.Ints(vals)

	return vals[len(vals)-1] - vals[0]
}

func naive(input []string) int {
	polymer := strings.TrimSpace(input[0])

	rules := map[string]string{}

	for i := 2; i < len(input); i++ {
		mapping := strings.Split(input[i], " -> ")
		rules[mapping[0]] = strings.TrimSpace(mapping[1])
	}

	for i := 0; i < 10; i++ {
		fmt.Println(i)
		for j := len(polymer)-1; j > 0; j-- {
			key := string(polymer[j-1]) + string(polymer[j])

			if substr, ok := rules[key]; ok {
				polymer = polymer[:j] + substr + polymer[j:]
			}
		}
	}

	letters := map[rune]int {}

	for _, char := range polymer {
		if _, ok := letters[char]; !ok {
			letters[char] = 1
		} else {
			letters[char]++
		}
	}

	var vals []int

	for _, val := range letters {
		vals = append(vals, val)
	}

	sort.Ints(vals)

	return vals[len(vals)-1] - vals[0]
}
```

## Day 15

Day 15 ought to be pretty simple - it is a classic pathfinding algorithm. When I looked at it, I even knew that I probably wanted to use
the [Dijkstra's shortest path algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) which is more than can be said for the
other graph traversal problem (which I eventually figured out called for either depth or breadth first search) early in the challenge.
Still, I really struggled to implement this one effectively at all, and as mentioned above, my solution is incredibly slow, taking
something in the region of 45 minutes to run. The problem itself is pretty straightforward; given a grid of weights, find the least
expensive path between the top left point and then two other points that are diagonally down and right.

```html
Example input:
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
```

```go
type coord struct {
	x, y int
}

type node struct {
	edges []coord
	weight int
}

func Fifteen(input []string) (int, int) {
	grid := map[coord]node{}

    // holds the weighted distance from the starting node for each other node
	dist := map[coord]int{}

    // holds all the nodes to check
    // the map[type]struct{}{} type essentially functions like a hashset
    // because looking up a key in a map in Golang is quicker than
    // handrolling a slice.Contains() method and struct{} won't get
    // allocated any memory
	queue := map[coord]struct{}{}

    // holds all the nodes we've visited
	visited := map[coord]struct{}{}

	for y, row := range input {
		rs := []rune(row)
		for x, r := range rs {
			if r == '\r' { continue }

			for i := 0; i < 5; i++ {
				for j := 0; j < 5; j++ {
					c := coord{x + len(strings.TrimSpace(input[0]))*i, y + len(input)*j}

					weight := int(r) - '0' + i + j
					if weight > 9 {
						weight = 1 + weight % 10
					}

					grid[c] = newNode(c, coord{len(strings.TrimSpace(input[0])) * 5, len(input) * 5}, weight)

                    // adds the node to the queue
					queue[c] = struct{}{}
				}
			}
		}
	}

    // set the initial coordinate to the source node
	dist[coord{0,0}] = 0

	for len(queue) > 0 {
		v := getSmallestDist(dist, visited)
        // delete node from queue
		delete(queue, v)
        // and add it to visited
		visited[v] = struct{}{}

		for _, u := range grid[v].edges {
            // for each adjacent node, if no distance has been calculated
            // (ie set to inf in classical algo) or the tentative distance
            // is shorted, then update the distance for the neighbouring node
			if _, ok := dist[u]; !ok || dist[v] + grid[u].weight < dist[u] {
				dist[u] = dist[v] + grid[u].weight
			}
		}
	}

	return dist[coord{len(strings.TrimSpace(input[0])) - 1, len(input) - 1}],
    dist[coord{len(strings.TrimSpace(input[0])) * 5 - 1, len(input) *5 - 1}]
}

// This is where the problem lies... while the dist map is small at the beginning,
// each call to this function takes >1ms, but as dist approaches its max value of
// 250000, each call takes ~11ms instead 
func getSmallestDist(dist map[coord]int, visited map[coord]struct{}) coord {
	smallestDist := math.MaxInt32
	var smallestCoord coord

    // looping through a map to find the smallest value is obviously
    // incredibly inefficient, and suggests I should use a different
    // data structure for dist
	for key, val := range dist {
		if _, ok := visited[key]; !ok {
			if val < smallestDist {
				smallestDist = val
				smallestCoord = key
			}
		}
	}

	return smallestCoord
}

func newNode(c, max coord, weight int) node {
	edges := []coord{}

	if c.x > 0 {
		edges = append(edges, coord{c.x-1, c.y})
	}

	if c.x < max.x {
		edges = append(edges, coord{c.x+1, c.y})
	}

	if c.y > 0 {
		edges = append(edges, coord{c.x, c.y-1})
	}

	if c.y < max.y {
		edges = append(edges, coord{c.x, c.y+1})
	}

	return node{edges, weight}
}
```