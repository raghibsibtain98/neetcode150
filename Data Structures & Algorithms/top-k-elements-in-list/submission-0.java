class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int[] result = new int[k];

        Map<Integer, Integer> map = new HashMap<>();

        PriorityQueue<Map.Entry<Integer,Integer>> pq = new PriorityQueue<>((e1,e2) -> {

            if (e1.getValue()!=e2.getValue()){
                return Integer.compare(e2.getValue(),e1.getValue());
            }
            return Integer.compare(e1.getKey(),e2.getKey());
        });

        for (int num: nums){
            map.put(num, map.getOrDefault(num,0)+1);
        }

        for (Map.Entry<Integer,Integer> entry : map.entrySet()){
            pq.add(entry);
        }

        while(k>0){
            Map.Entry<Integer,Integer> entry = pq.poll();
            k--;
            result[k] = entry.getKey();
        }

        return result;
    }
}
