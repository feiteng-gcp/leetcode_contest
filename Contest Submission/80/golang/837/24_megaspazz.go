func mostCommonWord(paragraph string, banned []string) string {
    ban := make(map[string]bool)
    for _, w := range banned {
        ban[w] = true
    }
    bestWord := ""
    bestCnt := 0
    freq := make(map[string]int)
    var sofar []rune
    for _, w := range (paragraph + " ") {
        c := unicode.ToLower(w)
        if !unicode.IsLetter(c) {
            if len(sofar) > 0 {
                s := string(sofar)
                if !ban[s] {
                    freq[s]++
                    if (freq[s] > bestCnt) {
                        bestWord = s
                        bestCnt = freq[s]
                    }
                }
            }
            sofar = nil
        } else {
            sofar = append(sofar, c)
        }
        // s := strings.ToLower(w)
        // if ban[s] {
        //     continue
        // }
        // freq[s]++
        // if (freq[s] > bestCnt) {
        //     bestWord = s
        //     bestCnt = freq[s]
        // }
    }
    return bestWord
}