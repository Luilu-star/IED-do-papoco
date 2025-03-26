public class goiaba{
    
    private int numeros[][];
    private String palavras[][];
    private double doubles[][];
    private int indexcolunas;
    private int indexlinhasi;
    private int indexlinhasS;
    private int indexlinhasd;

    public goiaba(int linha, int coluna){
        this.indexlinhasi = linha;
        this.indexlinhasS = linha;
        this.indexlinhasd = linha;
        this.indexcolunas = coluna;
        this.numeros = new int[linha][coluna];
        this.palavras = new String[linha][coluna];
        this.doubles =  new double[linha][coluna];
    }

    //Int

    public void adicionar(int valor, int linha, int coluna){
        if (linha < indexlinhasi && linha >= 0 && coluna < indexcolunas && coluna >= 0){
            numeros[linha][coluna] = valor;
        } else {
            System.out.println("Índice não encontrado!");
        }
    }

    public void deletarintnull(int linha, int coluna){
        numeros[linha][coluna] = 0;
    }

    public void deletarint(int linha, int coluna){
        numeros[linha][coluna] = numeros[linha][coluna];
        indexlinhasi--;
    }

    public void exibirint(){
        for(int l = 0; l < indexlinhasi; l++){
            for(int c = 0; c < indexcolunas; c++){
                System.out.print("[ " + numeros[l][c] + " ]");
            } 
            System.out.println();
        }
        System.out.println("Tamanho: " + indexlinhasi + " por " + indexcolunas);

    }

    //Strings
    
    public void adicionar(String nome, int linha, int coluna){
        if (linha < indexlinhasS && linha >= 0 && coluna < indexcolunas && coluna >= 0){
            palavras[linha][coluna] = nome;
        } else {
            System.out.println("Índice não encontrado!");
        }
    }

    public void deletarStrnull(int linha, int coluna){
        palavras[linha][coluna] = "null";
    }

    public void deletarStr(int linha, int coluna){
        palavras[linha][coluna] = palavras[linha][coluna];
        indexlinhasS--;
    }

    public void exibirStr(){
        for(int l = 0; l < indexlinhasS; l++){
            for(int c = 0; c < indexcolunas; c++){
                System.out.print("[ " + palavras[l][c] + " ]");
            } 
            System.out.println();
        }
        System.out.println("Tamanho: " + indexlinhasS + " por " + indexcolunas);
    }

    //Doubles

    public void adicionar(double value, int linha, int coluna){
        if (linha < indexlinhasd && linha >= 0 && coluna < indexcolunas && coluna >= 0){
            doubles[linha][coluna] = value;
        } else {
            System.out.println("Índice não encontrado!");
        }
    }

    public void deletardoubnull(int linha, int coluna){
        doubles[linha][coluna] = 0;
    }

    public void deletardoub(int linha, int coluna){
        doubles[linha][coluna] = doubles[linha][coluna];
        indexlinhasd--;
    }

    public void exibirdoub(){
        for(int l = 0; l < indexlinhasd; l++){
            for(int c = 0; c < indexcolunas; c++){
                System.out.print("[ " + doubles[l][c] + " ]");
            } 
            System.out.println();
        }
        System.out.println("Tamanho: " + indexlinhasd + " por " + indexcolunas);

    }
    
    public static void main(String[] args) {
        goiaba goiabada = new goiaba(3, 3);

        goiabada.adicionar(9, 0, 0);
        goiabada.adicionar(2, 0, 2);
        goiabada.adicionar(9, 1, 1);
        goiabada.adicionar(6, 2, 2);

        System.out.println("Matriz int:");
        System.out.println("--------------------");
        System.out.println("Int");
        goiabada.exibirint();
        System.out.println("--------------------");
        System.out.println("Removenull");
        goiabada.deletarintnull(0, 0);
        goiabada.exibirint();
        System.out.println("--------------------");
        System.out.println("Removetam");
        goiabada.deletarint(0, 0);
        goiabada.exibirint();
        System.out.println("--------------------");
        System.out.println();

        goiabada.adicionar("manga", 0, 0);
        goiabada.adicionar("banana", 0, 2);
        goiabada.adicionar("acelora", 1, 1);
        goiabada.adicionar("macarujá", 2, 2);

        System.out.println("Matriz String:");
        System.out.println("String");
        goiabada.exibirStr();
        System.out.println("--------------------");
        System.out.println("Removenull");
        goiabada.deletarStrnull(0, 0);
        goiabada.exibirStr();
        System.out.println("--------------------");
        System.out.println("Removetam");
        goiabada.deletarStr(0, 0);
        goiabada.exibirStr();
        System.out.println("--------------------");
        System.out.println();

        goiabada.adicionar(9.2, 0, 0);
        goiabada.adicionar(2.4, 0, 2);
        goiabada.adicionar(3.14, 1, 1);
        goiabada.adicionar(9.8, 2, 2);

        System.out.println("Matriz doubles:");
        System.out.println("--------------------");
        System.out.println("Doubles");
        goiabada.exibirdoub();
        System.out.println("--------------------");
        System.out.println("Removenull");
        goiabada.deletardoubnull(0, 0);
        goiabada.exibirdoub();
        System.out.println("--------------------");
        System.out.println("Removetam");
        goiabada.deletardoub(0, 0);
        goiabada.exibirdoub();
        System.out.println("--------------------");
        System.out.println();
    }
}