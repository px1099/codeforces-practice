//go:build ignore
package main
import "fmt"

func solve() {
	var w int
	fmt.Scan(&w)
	if w % 4 == 0 {
		fmt.Println("YES")
		return
	}
	fmt.Println("NO")
}

func main() {
	tc := 1
	// fmt.Scan(&tc)
	for t := 1; t <= tc; t++ {
		// fmt.Print("Case ", t, ": ")
		solve()
	}
}
