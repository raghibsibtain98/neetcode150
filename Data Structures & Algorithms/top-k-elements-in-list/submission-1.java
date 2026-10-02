class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int[] result = new int[k];

        Map<Integer, Integer> map = new HashMap<>();

        // PriorityQueue<Map.Entry<Integer,Integer>> pq = new PriorityQueue<>((e1,e2) -> {

        //     if (e1.getValue()!=e2.getValue()){
        //         return Integer.compare(e2.getValue(),e1.getValue());
        //     }
        //     return Integer.compare(e1.getKey(),e2.getKey());
        // });

        PriorityQueue<Map.Entry<Integer,Integer>> minHeap = 
        new PriorityQueue<>(Comparator.comparingInt(Map.Entry::getValue));

        for (int num: nums){
            map.put(num, map.getOrDefault(num,0)+1);
        }

        // for (Map.Entry<Integer,Integer> entry : map.entrySet()){
        //     pq.add(entry);
        // }

        for (Map.Entry<Integer,Integer> entry : map.entrySet()){
            minHeap.offer(entry);

            if (minHeap.size()>k){
                minHeap.poll();
            }
        }

        while(k>0){
            Map.Entry<Integer,Integer> entry = minHeap.poll();
            k--;
            result[k] = entry.getKey();
        }

        return result;
    }
}
