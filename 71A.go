//go:build ignore
package main
import "fmt"
import "strconv"

func solve() {
	var word string
	fmt.Scan(&word)
	if len(word) <= 10 {
		fmt.Println(word)
		return
	}
	abb := string(word[0]) + strconv.Itoa(len(word)-2) + string(word[len(word)-1])
	fmt.Println(abb)
}

func main() {
	tc := 1
	fmt.Scan(&tc)
	for t := 1; t <= tc; t++ {
		// fmt.Print("Case ", t, ": ")
		solve()
	}
}
