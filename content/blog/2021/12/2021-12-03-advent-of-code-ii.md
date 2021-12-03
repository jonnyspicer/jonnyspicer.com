---
type: blog
date: "2021-12-03T16:14:16Z"
author: Jonny Spicer
title: "Advent of Code II"
categories:
- Programming
series: ["Advent of Code"]
extras: prismjs
---
I solved the problems for days 1-3 of advent of code relatively straightforwardly, although my initial solution for today's part two was pretty heinous so has been refactored for below (you can see the original spaghetti [here](https://github.com/jonnyspicer/advent-of-code/commit/51543dfc7ec6823c672a453d38c3c298ee549f00#diff-b1d347b56463162cb64ed58f2e1d59261674d348f096c041c97104d5ae77aa56)). Each of the problems is run using code that looks like the following (with the `main` function tweaked slightly depending on the signature of the function its calling):

```go
func main() {
	// will clean this up to just take an day number
	rows := parseTxt("day/three.txt")
	a, b := day.Three(rows)
	fmt.Printf("Part one: %v\n", a)
	fmt.Printf("Part two: %v\n", b)
}

func parseTxt(path string) []string {
	rows, err := ioutil.ReadFile(path)
	if err != nil {
		fmt.Println(err)
	}

	return strings.Split(string(rows), "\n")
}
```

## Day 1

The problem for day one involves parsing a sliding window of values in a slice, and returning the number of times the window increases as
the slice is traversed. In the first part of the solution, the size of the window is only 1, and in the second, it's two.

```html
Example input:
199
200
208
210
200
207
240
269
260
263
```

```go
func One(readings []int, windowSize int) int {
	count := 0

	for i := windowSize; i < len(readings); i++ {
		if readings[i] > readings[i - windowSize] {
			count++
		}
	}

	return count
}
```

Seeing as the window is only ever moving one element along at a time, it's not necessary to compare the sum of all elements in the window,
and instead we can simply compare the first element of the first window to the last element of the second window.

## Day 2

Day two's challenges involve parsing instructions in two different ways. For part one, `forward x` increases horizontal position by `x`,
`down x` increases depth by `x` units and `up x` decreases depth by `x` units. For part two, there is a third variable, `aim`, and the rules
are as follows: `down x` increases your aim by `x` units, `up x` decreases your aim by `x` units, and `forward x` does two things - increases horizontal position by `x` units and increases depth by `aim * x`.

```html
Example input:
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

```go
// It was pointed out to me that passing a function as a
// parameter here is not desperately readable and it would 
// probably be better to refactor this to take an interface instead
func Two(
    input []string,
    navigate func(x, y, z *int, direction string, distance int)
) int {
	x, y, z := 0, 0, 0

	for _, move := range input {
		directions := strings.Split(move, " ")
		distance, _ := strconv.Atoi(directions[1])
		navigate(&x, &y, &z, directions[0], distance)
	}

	return x * y
}

func A(x, y, z *int, direction string, distance int) {
	switch direction {
	case "forward":
		*x += distance
	case "down":
		*y += distance
	case "up":
		*y -= distance
	}
}

func B(x, y, z *int, direction string, distance int) {
	switch direction {
	case "forward":
		*x += distance
		*y += distance * *z
	case "down":
		*z += distance
	case "up":
		*z -= distance
	}
}
```

## Day 3

This one already posed me a bit of a challenge - which doesn't bode well for my chances over the next 22 days. We are given a list of binary
numbers, and in part one, we must calculate both the most common and least common bits in every position. In part two, we calculate the
most and least common bits in every position, except that for both most and least common, for every element in the list, if the bit at the
relevant position is not the most/least common respectively then that element is removed from the last, and most/least common needs to be
recalculated accordingly, which tripped me up quite a bit upon reading the question.

```html
Example input:
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

```go
func Three(input []string) (int64, int64) {
	length := 12

	// part 1

	gamma := make([]rune, length)
	epsilon := make([]rune, length)
	m := make(map[int]int, length)

	for _, row := range input {
		bits := []rune(row)

		for i := 0; i < length; i++ {
			if bits[i] == '1' {
				m[i]++
			} else {
				m[i]--
			}
		}
	}

	for j := 0; j < length; j++ {
		if m[j] > 0 {
			gamma[j] = '1'
			epsilon[j] = '0'
		} else {
			gamma[j] = '0'
			epsilon[j] = '1'
		}
	}

	g, _ := strconv.ParseInt(string(gamma), 2, 64)
	e, _ := strconv.ParseInt(string(epsilon), 2, 64)

	// part two

	oxygenNumbers := lastRemainingString(input, length, oxygen)
	co2Numbers := lastRemainingString(input, length, carbon)

	oxygenString := ratingFromMap(oxygenNumbers, input)
	carbonString := ratingFromMap(co2Numbers, input)

	o, _ := strconv.ParseInt(oxygenString[0:length], 2, 64)
	c, _ := strconv.ParseInt(carbonString[0:length], 2, 64)

	return g * e, o * c
}
// returns 0 if there is no mcb,
// a positive value if the mcb is 1
// and a negative value if the mcb is 0
func mostCommonBit(
    m map[int]bool, 
    input []string, 
    position int
    ) int {
	count := 0

	for key, val := range m {
		if val {
			if input[key][position] == '1' {
				count++
			} else {
				count--
			}
		}
	}

	return count
}

func oxygen(r rune, mcb int) bool {
	return (r == '1' && mcb > 0) ||
    (r == '0' && mcb < 0 ) ||
    r == '1' && mcb == 0
}

func carbon(r rune, mcb int) bool {
	return (r == '1' && mcb < 0)
    || (r == '0' && mcb > 0 )
    || r == '0' && mcb == 0
}

// will return a map with only a single value of true,
// where the corresponding key is the index
// in the input slice that we're interested in
func lastRemainingString(
    input []string, 
    length int, 
    eval func(r rune, mcb int) bool) 
    map[int]bool {
	// first create a map of all the indexes 
    // where every value is true
	// seeing as we want to start with all the binary numbers
	m := map[int]bool{}
	for k := 0; k < len(input); k++ {
		m[k] = true
	}

	for l := 0; l < length; l++ {
		count := 0
		mcb := mostCommonBit(m, input, l)
		// for every binary number in the input
		for n, in := range input {
			// if our evaluation is false or
            // if the value in the map is already false
			if !eval(rune(in[l]), mcb) || !m[n] {
				m[n] = false
			}
		}

		// loop over our map again to see
        // if we only have one number left
		for _, val := range m {
			if val {
				count++
			}
		}

		if count == 1 {
			break
		}
	}

	return m
}

func ratingFromMap(m map[int]bool, input []string) string {
	for k, v := range m {
		if v {
			return input[k]
		}
	}

	return ""
}
```

The other thing that tripped me up for quite a while was comparing a rune to an int rather than another rune, ie `rune(in[i]) == 1` and
not realising what I was doing. Of course this will still compile and evaluate just fine, but I am comparing `1` to the unicode value of
the rune, (eg 48 for '0' or 49 for '1') so it won't do what I had expected. The important thing is that I got there in the end...