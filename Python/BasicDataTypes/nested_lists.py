if __name__ == '__main__':
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]
    second_lowest = sorted(set([grade for name, grade in students]))[1]
    print('\n'.join([name for name, grade in sorted(students) if grade == second_lowest]))