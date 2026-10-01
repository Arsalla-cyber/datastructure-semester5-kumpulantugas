import time

# 1. Pendekatan Memoization (Top-Down)
def count_ways_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    # Base cases: untuk n = 1 -> 1 cara, untuk n = 2 -> 2 cara
    if n <= 2:
        return n
    
    if n not in memo:
        # Relasi rekurens: f(n) = f(n-1) + f(n-2)
        memo[n] = count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo)
        
    return memo[n]


# 2. Pendekatan Tabulation (Bottom-Up)
def count_ways_tab(n):
    if n <= 2:
        return n
    
    # Inisialisasi tabel DP
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # Mengisi tabel dari bawah ke atas
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]


# 3. Pengujian Fungsi untuk n = 5, 10, dan 20
print("=== Pengujian Hasil (n = 5, 10, 20) ===")
test_values = [5, 10, 20]
for n in test_values:
    res_memo = count_ways_memo(n)
    res_tab = count_ways_tab(n)
    print(f"n = {n:2d} | Memoization: {res_memo:5d} | Tabulation: {res_tab:5d} | Sama? {res_memo == res_tab}")

# 4. Bonus: Perbandingan Waktu Eksekusi untuk n = 30
print("\n=== Bonus: Perbandingan Waktu Eksekusi (n = 30) ===")
n_bonus = 30

# Ukur waktu Memoization
start_time = time.perf_counter()
res_memo_30 = count_ways_memo(n_bonus)
end_time = time.perf_counter()
time_memo = (end_time - start_time) * 1000  # ms

# Ukur waktu Tabulation
start_time = time.perf_counter()
res_tab_30 = count_ways_tab(n_bonus)
end_time = time.perf_counter()
time_tab = (end_time - start_time) * 1000  # ms

print(f"n = {n_bonus}")
print(f"Hasil Memoization : {res_memo_30} (Waktu: {time_memo:.4f} ms)")
print(f"Hasil Tabulation  : {res_tab_30} (Waktu: {time_tab:.4f} ms)")