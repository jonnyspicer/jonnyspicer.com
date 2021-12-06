---
type: blog
date: "2021-12-06T08:01:44Z"
author: Jonny Spicer
title: "Advent of Code III"
categories:
- Programming
series: ["Advent of Code"]
extras: prismjs
---
The problems are slowly beginning to get harder, although I did find these three still very achievable. With a little bit of practice I am
finding my approach to solving them is improving very fast, and I am better at mentally modelling how the code should look, as well as
improving my understanding of Go - I feel like I am finally making progress grokking addresses and pointers thanks to these challenges.

## Day 4

The challenge for day four was to take a set of called numbers and a set of bingo cards, and calculate which bingo card would win first,
and then which would win last. The "score" for that card was produced by multiplying the last number that had been called before the card
won by the sum of all the uncalled numbers remaining on the card. Overall this one was pretty easy, once I got past a small hiccough with
my logic in the `iswinner()` method.

```html
Example input:
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
```

```go
type bingo struct {
	values [25]int
	called [25]bool
	turnsToWin int
	lastNumberCalled int
	unmarkedSum int
}

func Four(input []string) (int, int) {
	bingos := []bingo{}

	m := input[0]

    // ignore the first two lines as these are
    // the numbers called and whitespace and
    // then increment by six to account for more
    // blank lines
	for i := 2; i < len(input); i += 6 {
		bingoStringo := strings.Join(input[i:i+5], "")
        // probably my favourite line of code I've ever written
		bingos = append(bingos, stringoToBingo(bingoStringo, m))
	}

	fastestBingo := bingos[0]
	slowestBingo := bingos[0]

	for _, b := range bingos {
		if b.turnsToWin < fastestBingo.turnsToWin {
			fastestBingo = b
		}
		if b.turnsToWin > slowestBingo.turnsToWin {
			slowestBingo = b
		}
	}

	return fastestBingo.lastNumberCalled * fastestBingo.unmarkedSum,
    slowestBingo.lastNumberCalled * slowestBingo.unmarkedSum
}

func (b bingo) isWinner() bool {
	for i := 0; i < 5; i++ {
		if (
            // horizontal
            b.called[5*i] && 
            b.called[5*i+1] && 
            b.called[5*i+2] && 
            b.called[5*i+3] && 
            b.called[5*i+4]
        ) || (
            // vertical
            b.called[i] && 
            b.called[i+5] &&
            b.called[i+10] && 
            b.called[i+15] && 
            b.called[i+20] ) {
			return true
		}
	}

	return false
}

func stringoToBingo(s, m string) bingo {
	b := bingo{}
	vals := strings.Fields(s)
	for i := 0; i < 25; i++ {
		b.values[i], _ = strconv.Atoi(vals[i])
	}
	b.numberOfTurnsToWin(m)
	return b
}

func (b *bingo) numberOfTurnsToWin(nums string) {
	// parse nums
	// for each one, mark as seen && check winner
	// if winner, mark last number
	// calculate everything else

    // kinda gross but kinda funny
    // I later wrote a helper method
    // that you'll see later for this
	fakeJson := "[" + nums + "]"
	var moves []int
	_ = json.Unmarshal([]byte(fakeJson), &moves)

	// for every move
	for i := 0; i < len(moves); i++ {
		// for every value
		for j := 0; j < len(b.values); j++ {
			if moves[i] == b.values[j] {
				b.called[j] = true
				if b.isWinner() {
					b.lastNumberCalled = moves[i]
					b.turnsToWin = i
					b.sum()
					return
				}
			}
		}
	}
}

func (b *bingo) sum() {
	sum := 0

	for i := 0; i < 25; i++ {
		if !b.called[i] {
			sum += b.values[i]
		}
	}

	b.unmarkedSum = sum
}
```

## Day 5

Today's challenge was to take a series of coordinates in the form `x1,y1 -> x2,y2` and find every point on the grid where two or more of
the lines intersected. For part one diagonal lines were ignored, for part two they weren't. Again after not quite getting my diagonal
logic correct out of the gate, this one was still fairly easy.

```html
Example input:
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

I started a `utils` package for this one, which for now only has one function in:

```go
func ExtractInts(s string) []int {
	var ints []int

	r, _ := regexp.Compile(`\d+`)
	matches := r.FindAllString(s, -1)

	for _, match := range matches {
		i, _ := strconv.Atoi(match)
		ints = append(ints, i)
	}

	return ints
}

```

```go
func Five(input []string) (int, int) {
	var ventLines []ventLine

	for _, vl := range input {
		ventLines = append(ventLines, stringToVentLine(vl))
	}

	return five(ventLines, false), five(ventLines, true)
}

type ventLine struct {
	x1, x2, y1, y2 int
}

func stringToVentLine(s string) ventLine {
	ints := utils.ExtractInts(s)

	return ventLine{
		x1: ints[0],
		x2: ints[2],
		y1: ints[1],
		y2: ints[3],
	}
}

func five(vls []ventLine, diagonals bool) int {
    // Doing it like this felt pretty gross
    // I could've iterated over the list of coordinates
    // to find the highest values and then make slices
    // from that, but that felt pretty gross too
	grid := [1000][1000]int{}

	for _, v := range vls {
		v.calculateVents(&grid, diagonals)
	}

	count := 0

	for _, x := range grid {
		for _, y := range x {
			if y > 1 { count++ }
		}
	}

	return count
}

func (v ventLine) calculateVents(
    grid *[1000][1000]int,
    diagonals bool) {
	if v.x1 != v.x2 && v.y1 != v.y2 {
		if diagonals { v.diagonal(grid) }
	} else {
		v.straight(grid)
	}
}

func (v ventLine) straight(grid *[1000][1000]int) {
	var xl, xu, yl, yu int

	if v.x2 < v.x1 {
		xl = v.x2
		xu = v.x1
	} else {
		xl = v.x1
		xu = v.x2
	}

	if v.y2 < v.y1 {
		yl = v.y2
		yu = v.y1
	} else {
		yl = v.y1
		yu = v.y2
	}

	for x := xl; x <= xu; x++ {
		for y := yl; y <= yu; y++ {
			grid[x][y]++
		}
	}
}

// there is definitely a more readable, more concise
// way of doing this
func (v ventLine) diagonal(grid *[1000][1000]int) {
	// x and y both ascend
	if v.x1 < v.x2 && v.y1 < v.y2 {
		for i := 0; i <= v.x2 - v.x1; i++ {
			grid[v.x1+i][v.y1+i]++
		}
	}

	// x ascends y descends
	if v.x1 < v.x2 && v.y1 > v.y2 {
		for i := 0; i <= v.x2 - v.x1; i++ {
			grid[v.x1+i][v.y1-i]++
		}
	}

	// x descends y ascends
	if v.x1 > v.x2 && v.y1 < v.y2 {
		for i := 0; i <= v.x1 - v.x2; i++ {
			grid[v.x1-i][v.y1+i]++
		}
	}

	// x and y both descend
	if v.x1 > v.x2 && v.y1 > v.y2 {
		for i := 0; i <= v.x1 - v.x2; i++ {
			grid[v.x1-i][v.y1-i]++
		}
	}
}
```

## Day 6

The challenge for day 6 was to model the population of a group of fish, assuming that each fish spawns a new fish every 7 days and that
if a fish is new it takes 9 days to spawn a new fish instead. The first part required the population to be calculated after 80 days, the
second after 256. Admittedly with this one I fell into old habits, and started writing code without adequately planning it, and so the
code that may have found me the answer for part one was nowhere near efficient enough to find an answer for part two unless I was
running some kind of crazy hardware, which obviously I'm not... I included it here for posterity, given I have refactored most of the
other code posted here to some extent.

```html
Example input:
3,4,3,1,2
```

```go
// This... is not good. My brain is bad in the morning.
func Six(input []string) (int, int) {
	var lf []lanternfish
	for _, days := range utils.ExtractInts(input[0]) {
		lf = append(lf, newFish(days))
	}

	for i := 0; i < 80; i++ {
		for _, fish := range lf {
			fish.processDay(&lf)
		}
	}

	return len(lf), 0
}

type lanternfish struct {
	daysUntilSpawn int
}

func newFish(dus int) lanternfish {
	return lanternfish{ daysUntilSpawn: dus }
}

func (lf *lanternfish) processDay(fishList *[]lanternfish) {
	*lf = newFish(lf.daysUntilSpawn - 1)
	if lf.daysUntilSpawn < 0 {
		lf.daysUntilSpawn = 6
		*fishList = append(*fishList, newFish(8))
	}
}
```

```go
// This is both easier to implement
// and easier to read afterwards...
// I regret not thinking about it first.
func Six(input []string) (int, int) {
	initialFish := utils.ExtractInts(input[0])

	return fishPop(initialFish, 80), fishPop(initialFish, 256)
}

func fishPop(in []int, days int) int {
	lf := map[int]int{
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
	}

	for _, timer := range in {
		lf[timer]++
	}

	for i := 0; i < days; i++ {
		t0 := lf[0]
        t1 := lf[1] 
        t2 := lf[2] 
        t3 := lf[3] 
        t4 := lf[4] 
        t5 := lf[5] 
        t6 := lf[6] 
        t7 := lf[7] 
        t8 := lf[8]
		lf[8] = t0
		lf[7] = t8
		lf[6] = t7 + t0
		lf[5] = t6
		lf[4] = t5
		lf[3] = t4
		lf[2] = t3
		lf[1] = t2
		lf[0] = t1
	}

	return lf[0] + lf[1] + lf[2] + lf[3] + 
    lf[4] + lf[5] + lf[6] + lf[7] + lf[8]
}
```
