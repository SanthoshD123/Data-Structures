public class Main
{
	public static void main(String[] args) {
		int n=10;
		fun(n);
	}
	public static void fun(int n){
	    if(n==0){
	        return ;
	    }
	    fun(n/2);
	    System.out.print(n%2);
	}
}
