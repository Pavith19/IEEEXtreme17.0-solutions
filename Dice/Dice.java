/* *
* Author: Pavith Bambaravanage
* URL: https://github.com/Pavith19
* */

import java.util.*;

public class Dice {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // number of dice
        int k = scanner.nextInt(); // max target sum
        
        long[] dp = new long[6*n + 1];
        dp[0] = 1;
        
        // Calculate probabilities for all possible sums
        for (int i = 0; i < n; i++) {
            long[] newDp = new long[6*n + 1];
            for (int j = 0; j <= 6*i; j++) {
                for (int face = 1; face <= 6; face++) {
                    newDp[j + face] = (newDp[j + face] + dp[j]) % MOD;
                }
            }
            dp = newDp;
        }
        
        // Calculate total probability
        long totalProb = 0;
        for (int i = 1; i <= Math.min(k, 6*n); i++) {
            totalProb = (totalProb + dp[i]) % MOD;
        }
        
        // Calculate final probability
        long numerator = totalProb;
        long denominator = modPow(k, MOD - 2, MOD); // Fermat's little theorem for modular inverse
        
        long result = (numerator * denominator) % MOD;
        
        System.out.println(result);
    }
    
    // Fast modular exponentiation
    static long modPow(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1)
                result = (result * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
}
