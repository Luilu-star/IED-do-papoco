import vetor.PrimeiroVetor;

public class App {
    public static void main(String[] args) throws Exception {
        PrimeiroVetor vetor = new PrimeiroVetor(5);

        for(int i = 0; i < 5; i++) {

            vetor.adicionar(10 + i);
        }
        vetor.exibir();
    }
}
