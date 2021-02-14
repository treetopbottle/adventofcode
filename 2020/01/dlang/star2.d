import std;

void main() {
    auto target = 2020;

    auto list = stdin
        .byLine
        .map!(l => l.to!int)
        .array;

    outer: foreach (nr1; list) {
        foreach (nr2; list) {
            foreach (nr3; list) {
                if (nr1 == nr2) {
                    continue;
                } else if (nr1 == nr3) {
                    continue;
                } else if (nr2 == nr3) {
                    continue;
                } else if (nr1 + nr2 + nr3 == target) {
                    writeln(nr1 * nr2 * nr3);
                    break outer;
                }
            }
        }
    }
}
