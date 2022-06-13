def main():
    N = int(input())
    L = []
    sec = 0
    for _ in range(N):
        a, b = map(int, input().split())
        L.append((a, b))
        sec += a / b  #この導火線全体が燃えるのに、a / b 秒かかります
        # print(sec)

    print(sec)
    rem = sec / 2
    print(rem)
    ans = 0

    for a, b in L:
        print(rem)
        if rem >= a / b:  # この導火線全体が燃えるかどうか
            print(a/b)
            ans += a  # a cm進みます
            rem -= a / b  # a / b 秒経過しました
        else:
            ans += rem * b  # 1秒あたりb cm 進むので、rem * b cm 燃えたところで 全体で S / 2 秒経過します
            break
        
    print(ans)


if __name__ == '__main__':
    main()