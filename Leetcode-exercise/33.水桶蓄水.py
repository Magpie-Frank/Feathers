class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        pq = []
        cnt = 0
        for i in range(n):
            if bucket[i] == 0 and vat[i]:
                cnt += 1
                bucket[i] += 1
            if vat[i] > 0:
                heapq.heappush(pq, [-((vat[i] + bucket[i] - 1) // bucket[i]), i])
        if not pq:
            return 0
        res = float('inf')
        while cnt < res:
            v, i = heapq.heappop(pq)
            v = -v
            res = min(res, cnt + v)
            if v == 1:
                break
            t = (vat[i] + v - 2) // (v - 1)
            cnt += t - bucket[i]
            bucket[i] = t
            heapq.heappush(pq, [-((vat[i] + bucket[i] - 1) // bucket[i]), i])
        return res
