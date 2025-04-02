package algorithm;

import java.util.Scanner;

public class dfsMatrix {

    static int edge;
    static int vertex;
    static int[][] map;
    static boolean[] visit;

    public static void main(){
        Scanner sc = new Scanner(System.in);
        vertex = sc.nextInt();
        edge = sc.nextInt();
        map = new int[vertex][vertex];
        visit = new boolean[vertex];

        for(int i=0; i<edge; i++){
            int start = sc.nextInt();
            int next = sc.nextInt();

            map[start][next] = 1;
            map[next][start] = 1;
        }

        
        System.out.println("this is DFS using adjacency matrix");
    }

    public static void dfsList(int start){
        visit[start] = true;
        System.out.println(start + " ");

        for (int i=0; i<vertex; i++){
            if (map[start][i] == 1 && visit[i] == false){
                dfsList(i);
            }
        }
    }
}
