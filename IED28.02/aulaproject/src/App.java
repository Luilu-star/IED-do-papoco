import vetor.PrimeiroVetor;

public class App {
    public static void main(String[] args) throws Exception {
        PrimeiroVetor vetor = new PrimeiroVetor(5);

        int [] valores = {10,20,30,40,50};
        for (int valor : valores) {
            vetor.adicionarTodos(valor);
        }
        
        vetor.getElemento(2);
        //System.out.println("Valor de índice 2: " + vetor.getElemento(2));
        System.out.println("Tamanho do vetor: " + vetor.getTamanho());
        System.out.println("--------------------------------");
        vetor.exibir();

        vetor.remove(2);
        System.out.println("--------------------------------");
        System.out.println("Tamanho do vetor: " + vetor.getTamanho());
        vetor.exibir();
    }
}
