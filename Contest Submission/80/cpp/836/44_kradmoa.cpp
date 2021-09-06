class Solution {
public:
    int racecar(int target) {
		int speedarr[32] = { -32768, -16384, -8192, -4096, -2048, -1024, -512, -256, -128, -64, -32, -16, -8, -4, -2, -1,
			1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 };

		// 15 : -1
		// 16 : 1

		//int dp[60000][32]; // -30000 ~ +29999
		char **dp;
		dp = new char*[30000];

		for (int i = 0; i < 30000; ++i)
		{
			dp[i] = new char[32];

			for (int j = 0; j < 32; ++j)
			{
				dp[i][j] = -1;
			}
		}

		dp[15000][16] = 0;

		queue<pair<int, char>> work;
		work.push(make_pair(15000, 16));

		while (true)
		{
			pair<int, char> current = work.front();
			work.pop();

			if (target + 15000 == current.first)
            {
                int ret = dp[current.first][current.second];
                
                for (int i = 0; i < 30000; ++i)
                    delete[] dp[i];
                delete[] dp;
                
				return ret;
            }

			// case 'A'
			int nextpos = current.first + speedarr[current.second];

			if (nextpos >= 0 && nextpos < 30000)
			{
				int nextspeed = current.second;
				if (current.second >= 16)
					nextspeed++;
				else
					nextspeed--;

				if (dp[nextpos][nextspeed] == -1)
				{
					dp[nextpos][nextspeed] = dp[current.first][current.second] + 1;
					work.push(make_pair(nextpos, nextspeed));
				}
			}

			// case 'R'
			int nextspeed = 15;
			if (current.second < 16)
				nextspeed = 16;

			if (dp[current.first][nextspeed] == -1)
			{
				dp[current.first][nextspeed] = dp[current.first][current.second] + 1;
				work.push(make_pair(current.first, nextspeed));
			}
		}
    }
};