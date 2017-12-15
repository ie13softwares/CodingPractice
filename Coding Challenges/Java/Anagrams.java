/* Given two strings, a and b , that may or may not be of the same length, determine the minimum 
number of character deletions required to make a and b anagrams. Any characters can be deleted 
from either of the strings. 
---------------------------------------------
Input:
Number of Test cases, followed by pair of strings for each test case.

Output:
Number of characters to be deleted. 

Program by:
Bala Krishna - pince.balakrishna@gmail.com
*/
 
import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Anagrams
{
	public static void main (String[] args) throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int T = Integer.parseInt(line);
 
 		while(T > 0){
			T--;
			String s1 = br.readLine().trim();
			String s2 = br.readLine().trim();
 
			String p1 = s1.replaceAll("\\s", "");
			String p2 = s2.replaceAll("\\s", "");
 
			String l1 = p1.toLowerCase();
			String l2 = p2.toLowerCase();
 
			int[] count = new int[26];
			for(int i=0; i<l1.length(); i++){
				count[l1.charAt(i)-97]++;
			}
			for(int j=0; j<l2.length(); j++){
				count[l2.charAt(j)-97]--;
			}
			int sum = 0;
			for(int k=0; k<26; k++){
				sum += abs(count[k]);
			}
 
			System.out.println(sum);
		}
	}
	static int abs(int a){
		if(a < 0){
			return (-a);
		}else{
			return a;
		}
	}
}
