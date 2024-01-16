import java.util.Arrays;
import java.util.Scanner;

public class Main{
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String[] arr = new String[5];

    for (int i = 0; i < arr.length; i++) {
        arr[i] = sc.nextLine();
    }

    String[] answer_list = new String[15];
    for (int i = 0; i < answer_list.length; i++) {
        if (answer_list[i] == null) answer_list[i] = "";
    }

    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr[i].length(); j++) {
            answer_list[j] += arr[i].charAt(j);
        }
    }

    String answer = "";
    for (String str : answer_list) {
        answer += str;
    }
    System.out.println(answer);
}
}