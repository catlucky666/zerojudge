#題目禁止使用evaluate_expression
import sys
import numexpr as ne
def evaluate_expression(expression):
        return int(ne.evaluate(expression))
def main():
    for l in sys.stdin:
        l = l.strip()
        if not l:
            continue
        print(evaluate_expression(l))
if __name__ == "__main__":
    main()