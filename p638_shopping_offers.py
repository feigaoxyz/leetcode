class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        for i, p in enumerate(price):
            row = [0 for _ in price] + [p]
            row[i] = 1
            special.append(row)
        # print(special)
        dp = dict()
        dp[tuple(0 for _ in price)] = 0
        dp_update = dict()
        dp_update.update(dp)
        for deal in special:
            *count, p = deal
            for item, item_p in dp.items():
                for times in range(1, 10):
                    new_item = tuple(
                        i + d * times for i, d in zip(item, count))
                    if any(i > n for i, n in zip(new_item, needs)):
                        break
                    else:
                        new_p = item_p + p * times
                        if (new_item not in dp_update
                                or dp_update[new_item] > new_p):
                            dp_update[new_item] = new_p
                        else:
                            break
            # dp = dp_update.copy()
            dp.update(dp_update)
            # print(deal, dp.items())

        # print(len(dp))
        return dp[tuple(needs)]


fn = Solution().shoppingOffers

print(fn([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]), 14)
print(fn([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]), 11)
print(fn([7,6,1,1,10,7],
[[4,6,6,2,2,6,29],[5,4,4,5,3,5,24],[0,4,6,1,2,0,9],[4,3,2,6,6,1,4],[2,4,6,6,3,4,30],[4,3,0,2,5,3,20],[1,1,0,6,6,4,16],[6,3,0,3,4,2,13],[3,3,6,4,1,6,21],[2,3,1,6,4,6,26],[3,2,3,2,4,3,16],[1,6,0,0,0,0,20],[4,1,5,5,4,4,19],[3,1,4,4,4,3,19],[0,2,1,3,5,5,22],[2,6,5,1,5,4,30],[5,4,5,0,3,1,18],[6,4,6,2,5,1,11],[1,2,1,1,5,0,23],[1,5,5,1,5,2,31],[1,6,3,5,1,0,12],[5,6,2,2,3,0,20],[2,6,2,1,2,1,2],[5,1,2,6,5,5,3],[1,5,2,2,2,5,15],[4,3,4,0,3,4,3],[6,2,4,6,0,4,2],[2,3,0,0,3,0,3],[1,6,6,0,4,6,2],[5,2,1,2,6,3,16],[0,0,0,6,1,4,14],[1,0,4,3,3,3,27],[4,3,5,3,0,2,17],[3,1,4,1,3,5,25],[0,1,1,5,6,1,12],[0,3,0,6,3,2,9],[5,5,1,0,2,6,14],[2,6,5,5,0,2,20],[2,0,0,0,6,6,11],[6,0,2,4,2,2,17],[5,2,2,1,1,4,12],[1,1,4,3,1,2,29],[6,5,4,1,3,3,24],[3,2,6,0,1,6,9],[3,6,4,6,1,0,11],[2,4,1,3,3,3,16],[4,5,3,4,1,5,19],[5,1,3,6,2,0,24],[3,6,6,6,5,4,5],[0,4,4,0,6,3,31],[2,6,0,5,3,1,12],[2,6,1,5,1,5,17],[1,3,1,4,3,1,8],[6,3,4,4,0,0,20],[4,3,0,4,1,0,5],[2,6,0,2,5,2,4],[4,5,5,5,1,5,10],[2,6,1,2,2,6,3],[0,6,2,2,0,2,4],[6,0,0,1,6,5,21],[3,0,3,0,3,1,31],[5,6,6,5,3,1,18],[3,0,3,1,4,3,24],[4,6,1,2,4,1,18],[2,6,3,5,5,6,7],[1,1,2,4,5,2,19],[2,3,6,3,1,2,23],[3,6,6,5,3,0,5],[5,1,2,0,6,5,30],[2,5,0,3,4,2,19],[0,2,2,0,3,6,16],[4,2,0,5,6,6,22],[0,0,4,5,6,6,23],[3,3,0,5,1,5,10],[3,1,1,3,3,1,12],[0,0,6,2,0,6,12],[6,5,3,4,5,0,31],[3,5,5,6,1,3,4],[0,2,5,3,3,4,22],[4,5,1,2,3,0,9],[4,6,2,1,3,5,28],[6,5,0,2,3,5,22],[4,1,5,2,1,3,25],[4,0,3,0,3,2,4],[6,3,5,1,0,0,13],[3,5,0,3,2,0,30],[3,3,5,6,2,1,27],[4,2,0,6,2,1,23],[3,3,2,3,6,5,12],[5,4,5,1,0,5,19],[2,3,6,6,4,2,16],[5,4,6,0,6,4,13],[0,5,4,3,2,4,11],[6,2,0,4,6,5,14],[0,4,6,0,5,3,18],[1,6,2,6,1,2,21],[5,4,5,5,3,2,29],[3,6,4,2,0,4,18],[4,1,2,4,3,1,14],[1,5,2,2,2,3,27]],
[6,6,6,6,6,6]))