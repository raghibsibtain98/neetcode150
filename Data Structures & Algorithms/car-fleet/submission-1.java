class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[][] combined = new Integer[n][2];

        for (int i = 0; i<n; i++){
            combined[i][0] = position[i];
            combined[i][1] = speed[i];
        }

        Arrays.sort(combined, new Comparator<Integer[]>() {
    @Override
    public int compare(Integer[] a, Integer[] b) {
        return Integer.compare(b[0], a[0]);
    }
});
        Stack<Double> timeStack = new Stack<>();
        for (Integer[] pair : combined){
            double time = (double) (target - pair[0])/pair[1] ; 
            timeStack.push(time);
            if (timeStack.size()>=2 
                && timeStack.get(timeStack.size()-1)<=timeStack.get(timeStack.size()-2) 
            ){
                timeStack.pop();
            }
        }

        return timeStack.size();
        
    }
}
