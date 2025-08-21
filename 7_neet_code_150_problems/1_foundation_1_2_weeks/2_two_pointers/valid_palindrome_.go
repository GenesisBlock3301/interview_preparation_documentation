package main

import (
	"fmt"
	"unicode"
)

func cleanupString(s string) string {
	result := make([]rune, 0, len(s))

	for _, r := range s {
		if unicode.IsLetter(r) || unicode.IsNumber(r) {
			result = append(result, unicode.ToLower(r))
		}
	}
	return string(result)
}

func isValidPalindrome(s string) bool {
	cStr := cleanupString(s)
	i := 0
	j := len(cStr) - 1
	for i < j {
		if cStr[i] != cStr[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func main() {
	str_ := "Was it a car or a cat I saw?"
	fmt.Println(isValidPalindrome(str_))
}
