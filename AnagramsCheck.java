/* Program to Check if two given Strings are anagrams or not.
----------
Input: 
The program receives two strings as inputs without any constraints. 
----------
Output:
"Anagrams" - If the given strings are Anagrams
"Not Anagrams" - If not anagrams. 

Note:
The Program treats Special characters and numbers as viable characters to form a sentence. 

Code Written by:
Bala Krishna @prince.balakrishna

*/

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line1 = br.readLine().trim();
		String line2 = br.readLine().trim();
		
		
		String l1 = line1.replaceAll("\\s", "");
		String l2 = line2.replaceAll("\\s", "");
		
		
		
		if(l1.length() == l2.length()){
			
			//System.out.println(l1);
			//System.out.println(l2);
			
			char[] s1 = l1.toLowerCase().toCharArray();
			char[] s2 = l2.toLowerCase().toCharArray();
			
			Arrays.sort(s1);
			Arrays.sort(s2);
			
			if(Arrays.equals(s1, s2)){
				System.out.println("Anagrams");
			}
			else{
				System.out.println("Not Anagrams");
			}
		}else{
			System.out.println("Not Anagrams");
		}
		
	}
}
