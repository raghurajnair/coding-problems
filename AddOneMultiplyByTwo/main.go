package main

import "fmt"

func AddOne(c chan int, numtoadd int) {
	c <- (numtoadd + 1)
}

func MultiplyByTwo(c chan int, numtomultiply int) {
	c <- numtomultiply * 2
}

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	result := make([]int, len(numbers))
	input_channel := make(chan int, len(numbers))
	output_channel := make(chan int, len(numbers))

	for i := 0; i < len(numbers); i++ {
		go AddOne(input_channel, numbers[i])
	}

	for i := 0; i < len(numbers); i++ {
		go MultiplyByTwo(output_channel, numbers[i])
	}

	for i := 0; i < len(numbers); i++ {
		result[i] = <-output_channel
	}

	fmt.Println(result)

}
