public class string1 {

    public static void main(String[] args) {

        String nome = "Jurupebas";
        int anos = 23;
        System.out.println(nome + " tem " + anos + " anos");

     //***********************************************************//

        String str = new String("Gabriel");
        String str2 = new String("Milao");

        System.out.println(str + " " + str2);

        System.out.println(str.concat(str2).toUpperCase() + " | " + "Está é a concatenação");
        System.out.println("Quantidade de caracteres: " + str.length());
    }
}