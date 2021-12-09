---
type: blog
date: "2021-12-09T17:48:53Z"
author: Jonny Spicer
title: "Advent of Code IV"
categories:
- Programming
series: ["Advent of Code"]
---
After three more days of AoC, I am starting to feel the difficulty a bit. Whilst I did manage to find solutions to all three of the problems
below, none of them are optimal, and all took me longer than I'd like to admit.

## Day 7
Day 7 was fortunately still pretty straightforward with a good knowledge of primary school mathematics. Given a group of positions in a
single plane, you first have to find the smallest number of moves to have them all reach a single position if each moves costs `1`, and then
if each subsequent moves costs an additional one (i.e. initially moving `3` costs `3`, then subsequently moving `3` costs `1 + 2 + 3 = 6`).

```html
Example input:
16,1,2,0,4,2,7,1,2,14
```

```go
// Very little explanation needed for this one!
func Seven(input []string) (int, int) {
	positions := utils.ExtractInts(input[0])
	med := median(positions)
	mea := mean(positions)
	medFuel, meaFuel := 0, 0

	for _, p := range positions {
		medFuel += int(math.Abs(float64(p - med)))
		for i := 0; i <= int(math.Abs(float64(p - mea))); i++ {
			meaFuel += i
		}
	}

	return medFuel, meaFuel
}

func median(input []int) int {
	sort.Ints(input)

	middle := len(input) / 2

	if middle % 2 == 1 {
		return input[middle]
	}

	return (input[middle-1] + input[middle]) / 2
}

func mean(input []int) int {
	sum := 0

	for _, i := range input {
		sum += i
	}

	return sum / len(input)
}
```

## Day 8
The explanation for day 8 is honestly such a mouthful that if you want to really understand what the problem is, you'll have to go look at
it yourself. Essentially you are presented with a set of codes that each correspond to a digit on a seven-segment display, with each letter
corresponding to a segment. Using the digits to the left of the pipe will allow you to decode those to the right - the first part of the
challenge requires you to calculate how many times the digits 1, 4, 7 or 8 appear and the second requires you to read the section to the
right of the pipe as a four-digit number, and find the product of all such numbers.

My code is, once again, not good, but here it is anyway.

```html
Example input:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

```go
func Eight(input []string) (int, int) {
	easyCount, hardCount := 0, 0
	for _, in := range input {
		parts := strings.Split(in, " | ")
		wires := strings.Fields(parts[0])
		output := strings.Fields(parts[1])

		// all possible values around the digit face
		possibleValues := map[int][]string{
			// top
			1: {"a", "b", "c", "d", "e", "f", "g"},
			// top left
			2: {"a", "b", "c", "d", "e", "f", "g"},
			// top right
			3: {"a", "b", "c", "d", "e", "f", "g"},
			// middle
			4: {"a", "b", "c", "d", "e", "f", "g"},
			// bottom left
			5: {"a", "b", "c", "d", "e", "f", "g"},
			// bottom right
			6: {"a", "b", "c", "d", "e", "f", "g"},
			// bottom
			7: {"a", "b", "c", "d", "e", "f", "g"},
		}

		dw := [10]bool{}
		// while we haven't figured out each of the inputs
		for decodedWires(dw) < len(wires) {
			// loop through them
			for i, w := range wires {
				if dw[i] == true {
					continue
				}

				switch len(w) {
				case 2:
					// digit is a 1
					possibleValues = updatePossibleValues(1, w, possibleValues)
					dw[i] = true

				case 3:
					// digit is a 7
					possibleValues = updatePossibleValues(7, w, possibleValues)
					dw[i] = true

				case 4:
					// digit is a 4
					possibleValues = updatePossibleValues(4, w, possibleValues)
					dw[i] = true

				case 5:
					// digit could be a 2, 3, 5
					two := couldBe(possibleValues, w, requiredSegments[2])
					three := couldBe(possibleValues, w, requiredSegments[3])
					five := couldBe(possibleValues, w, requiredSegments[5])

					if two && !three && !five {
						// it's a two
						possibleValues = updatePossibleValues(2, w, possibleValues)
						dw[i] = true
					} else if !two && three && !five {
						// it's a three
						possibleValues = updatePossibleValues(3, w, possibleValues)
						dw[i] = true
					} else if !two && !three && five {
						// it's a five
						possibleValues = updatePossibleValues(5, w, possibleValues)
						dw[i] = true
					}

				case 6:
					// digit could be a 0, 6 or 9
					zero := couldBe(possibleValues, w, requiredSegments[0])
					six := couldBe(possibleValues, w, requiredSegments[6])
					nine := couldBe(possibleValues, w, requiredSegments[9])

					if zero && !six && !nine {
						// it's a zero
						possibleValues = updatePossibleValues(0, w, possibleValues)
						dw[i] = true
					} else if !zero && six && !nine {
						// it's a six
						possibleValues = updatePossibleValues(6, w, possibleValues)
						dw[i] = true
					} else if !zero && !six && nine {
						// it's a nine
						possibleValues = updatePossibleValues(9, w, possibleValues)
						dw[i] = true
					}

				case 7:
					// digit is an 8
					dw[i] = true
				}
			}
		}

		sum := 0
		for i, o := range output {
			switch len(o) {
			case 2, 4, 3, 7:
				easyCount++
			}

			// raises the digit by a power of 10 to put it in the right place
			// rather than faff around with type conversions and concatenation
			sum += decodeDigit(o, possibleValues) * int(math.Pow(10, float64(len(output) - i - 1)))
		}

		hardCount += sum
	}
	return easyCount,hardCount
}

func updatePossibleValues(i int, s string, possibleValues map[int][]string) map[int][]string{
	// for every required segment
	for j := 0; j < len(requiredSegments[i]); j++ {
		// remove all the values that are no longer possible
		possibleValues[requiredSegments[i][j]] = reduceSlice(possibleValues[requiredSegments[i][j]], s)
	}

	return possibleValues
}

func decodedWires(s [10]bool) int {
	count := 0
	for _, b := range s {
		if b { count ++ }
	}
	return count
}

func decodeDigit(s string, m map[int][]string) int {
	switch len(s) {
	case 2:
		return 1
	case 3:
		return 7
	case 4:
		return 4
	case 5:
		if couldBe(m, s, requiredSegments[2]) { return 2 }
		if couldBe(m, s, requiredSegments[3]) { return 3 }
		if couldBe(m, s, requiredSegments[5]) { return 5 }
	case 6:
		if couldBe(m, s, requiredSegments[0]) { return 0 }
		if couldBe(m, s, requiredSegments[6]) { return 6 }
		if couldBe(m, s, requiredSegments[9]) { return 9 }
	}
	return 8
}

// removes all the chars from the slice that aren't present in the matching string
// doesn't necessarily reduce down to a single char like a javascript array.reduce()
func reduceSlice(sl []string, st string) []string {
	// for every element in the slice
	for i := len(sl)-1; i >= 0; i-- {
		// if the wire doesn't contain that element
		if !strings.Contains(st, sl[i]) {
			sl = removeElement(sl, i)
		}
	}

	return sl
}

func removeElement(s []string, i int) []string {
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}

// takes a map of all the current possible values, the wire string,
// the number we're interested in seeing if it could be and a slice of required values for that number
func couldBe(m map[int][]string, w string, s []int) bool {
	seen := map[int]bool{}
	reps := len(w)

	// the number of iterations here is fairly arbitrary
	for j := 0; j < reps; j++ {
		// for each value we need to fill
		for _, val := range s {
			// see how many options we have
			mr := matchingRunes([]rune(w), m[val])
			switch len(mr) {
			// if there's only one, remove that char from the string before continuing
			case 1:
				w = strings.Replace(w, string(mr[0]), "", -1)
				seen[val] = true
			// if there's none
			case 0:
				// and we haven't already filled the value
				if !seen[val] {
					return false
				}
			// if we still have multiple options left for multiple values
			default:
				// And aren't going to make any more progress by iterating more
				if j == reps - 1 {
					return true
				}
			}
		}
	}

	// if we don't have all the values we need
	for _, val := range s {
		if !seen[val] { return false }
	}

	return true
}

// gets all runes that appear in both slices
func matchingRunes(needles []rune, haystack []string) []rune {
	var rs []rune
	// for every character in the wire string
	for _, r := range needles {
		// for every element in the relevant map
		for _, elem := range haystack {
			if string(r) == elem { rs = append(rs, r) }
		}
	}
	return rs
}
```

## Day 9
For day 9, you are given a grid of digits and firstly have to identify the sum of all points who are bounded only by higher numbers
(diagonal bounds not included). The second part requires finding the size of the "basin" for each of those low points, i.e. the bounding
points which are higher than the initial low point, and then the points that are higher than those, and so on until the point in question is
a 9. You're than required to find the product of the size of the three largest basins.

```html
Example input:
2199943210
3987894921
9856789892
8767896789
9899965678
```

```go
package day

import (
	"sort"
)

type coord struct {
	x int
	y int
}

func Nine(input []string) (int, int) {
	grid := map[int][]int{}

	for i, line := range input {
		// convert to runes and save in slice
		rs := []rune(line)
		for _, r := range rs {
			if r == '\r' { continue }
			grid[i] = append(grid[i], int(r) - '0')
		}
	}

	sum := 0

	var lowPoints []coord

	// down the grid
	for i := 0; i < len(grid); i++ {
		// across the grid
		for j := 0; j < len(grid[0]); j++ {
			if lowPoint(grid, coord{j, i}) {
				lowPoints = append(lowPoints, coord{j, i})
				sum += 1 + grid[i][j]
			}
		}
	}

	var sizes []int

	// while there are points to check
	for _, lp := range lowPoints {
		// mark it as seen
		// check the other points, add them to seen
		// add them to list to be checked as well

		var basin []coord
		toBeChecked := []coord{lp}

		for len(toBeChecked) > 0 {
			for i := len(toBeChecked) - 1; i >= 0; i-- {
				tbc := toBeChecked[i]
				// check if its part of the basin
				// if it is, add it to the basin and add the relevant elements to tbc
				// remove tbc from to be checked

				if !contains(tbc, basin) && isInBounds(grid, tbc) && grid[tbc.y][tbc.x] != 9 {
					basin = append(basin, tbc)
					up := coord{tbc.x, tbc.y-1}
					down := coord{tbc.x, tbc.y+1}
					left := coord{tbc.x-1, tbc.y}
					right := coord{tbc.x+1, tbc.y}
					s := []coord{up, down, left, right}
					toBeChecked = append(toBeChecked, s...)
				}

				toBeChecked[i] = toBeChecked[len(toBeChecked)-1]
				toBeChecked = toBeChecked[:len(toBeChecked)-1]
			}
		}

		sizes = append(sizes, len(basin))
	}

	sort.Ints(sizes)

	return sum, sizes[len(sizes) - 1] * sizes[len(sizes) - 2] * sizes[len(sizes) - 3]
}

func isInBounds(m map[int][]int, c coord) bool {
	return c.x >= 0 && c.y >= 0 && c.x < len(m[0]) && c.y < len(m)
}

func lowPoint(m map[int][]int, c coord) bool {
	i, j := c.y, c.x
	if !isInBounds(m, coord{j, i}) { return false }

	var up, left, right, down bool
	// up
	if i > 0 {
		up = m[i][j] < m[i-1][j]
	} else {
		up = true
	}

	// left
	if j > 0 {
		left = m[i][j] < m[i][j-1]
	} else {
		left = true
	}

	// right
	if j < len(m[i]) - 1 {
		right = m[i][j] < m[i][j+1]
	} else {
		right = true
	}

	// down
	if i < len(m) - 1 {
		down = m[i][j] < m[i+1][j]
	} else {
		down = true
	}

	return up && left && right && down
}

func contains(needle coord, haystack []coord) bool {
	for _, hay := range haystack {
		if hay.x == needle.x && hay.y == needle.y { return true }
	}
	return false
}
```