public class arrozcomfeijao{
    private int vet1[];
    private int tamanhoint;
    private String vet2[];
    private int tamanhostr;
    private float vet3[];
    private int tamanhofloat;

    public arrozcomfeijao(int capacidade){
        this.vet1 = new int[capacidade];
        this.tamanhoint = 0;

        this.vet2 = new String[capacidade];
        this.tamanhostr = 0;

        this.vet3 = new float[capacidade];
        this.tamanhofloat = 0;
    }

    //INT
    public void adicionarint(int element) {
        if(tamanhoint < vet1.length) {
            vet1[tamanhoint] = element;
            tamanhoint++;
        } else {
            System.out.println("Vetor cheio!");
        }
    }

    public int returnTamanhoint(){
        return tamanhoint;
    }

    public void remove(int indice){
        if (indice < 0 || indice >= tamanhoint){
            System.out.println("Índice não encontrado.");
            return;
        }
        for (int i = indice; i < tamanhoint - 1; i++){
            vet1[i] = vet1[i+1];
        }
        tamanhoint--;
    }

    public void removenull(int indice){
        if (indice < 0 || indice >= tamanhoint){
            System.out.println("Índice não encontrado.");
            return;
        }
        vet1[indice] = 0;
    }

    public void mostrar() {
        System.out.println("Vetor1:");
        for (int i = 0; i < tamanhoint; i++){
            System.out.println(vet1[i]);
        }
        System.out.println();
    }

    //AQUI É STRING
    public void adicionarstr(String element) {
        if(tamanhostr < vet2.length) {
            vet2[tamanhostr] = element;
            tamanhostr++;
        } else {
            System.out.println("Vetor cheio!");
        }
    }

    public int returnTamanhostr(){
        return tamanhostr;
    }

    public void removestr(int indice){
        if (indice < 0 || indice >= tamanhostr){
            System.out.println("Índice não encontrado.");
            return;
        }
        for (int i = indice; i < tamanhostr - 1; i++){
            vet2[i] = vet2[i+1];
        }
        tamanhostr--;
    }

    public void removenullstr(int indice){
        if (indice < 0 || indice >= tamanhostr){
            System.out.println("Índice não encontrado.");
            return;
        }
        vet2[indice] = null;
    }

    public void mostrarstr() {
        System.out.println("Vetor2:");
        for (int i = 0; i < tamanhostr; i++){
            System.out.println(vet2[i]);
        }
        System.out.println();
    }

    //FLOATS AQUI Ó
    public void adicionarfloat(float element) {
        if(tamanhofloat < vet3.length) {
            vet3[tamanhofloat] = element;
            tamanhofloat++;
        } else {
            System.out.println("Vetor cheio!");
        }
    }

    public int returnTamanhofloat(){
        return tamanhofloat;
    }

    public void removefloat(int indice){
        if (indice < 0 || indice >= tamanhofloat){
            System.out.println("Índice não encontrado.");
            return;
        }
        for (int i = indice; i < tamanhofloat - 1; i++){
            vet3[i] = vet3[i+1];
        }
        tamanhofloat--;
    }

    public void removenullfloat(int indice){
        if (indice < 0 || indice >= tamanhofloat){
            System.out.println("Índice não encontrado.");
            return;
        }
        vet3[indice] = 0.0f;
    }

    public void mostrarfloat() {
        System.out.println("Vetor3:");
        for (int i = 0; i < tamanhofloat; i++){
            System.out.println(vet3[i]);
        }
        System.out.println();
    }

    public static void main (String[] args) {
        arrozcomfeijao vetores = new arrozcomfeijao(5);


        vetores.adicionarint(10);
        vetores.adicionarint(30);
        vetores.adicionarint(84623);
        vetores.adicionarint(23);
        vetores.adicionarint(123);
        System.out.println("--------------------------");
        vetores.mostrar();
        System.out.println("Tamanho:" + vetores.tamanhoint);
        System.out.println("--------------------------");
        vetores.remove(3);
        vetores.mostrar();
        System.out.println("Tamanho:" + vetores.tamanhoint);
        System.out.println("--------------------------");
        vetores.removenull(3);
        vetores.mostrar();
        System.out.println("Tamanho:" + vetores.tamanhoint);
        System.out.println("--------------------------");
       


        vetores.adicionarstr("Maçã");
        vetores.adicionarstr("Banana");
        vetores.adicionarstr("Siriguela");
        vetores.adicionarstr("Melancia");
        vetores.adicionarstr("Maraujá");
        vetores.mostrarstr();
        System.out.println("Tamanho:" + vetores.tamanhostr);
        System.out.println("--------------------------");
        vetores.removestr(3);
        vetores.mostrarstr();
        System.out.println("Tamanho:" + vetores.tamanhostr);
        System.out.println("--------------------------");
        vetores.removenullstr(3);
        vetores.mostrarstr();
        System.out.println("Tamanho:" + vetores.tamanhostr);
        System.out.println("--------------------------");



        vetores.adicionarfloat(1.89f);
        vetores.adicionarfloat(2.3f);
        vetores.adicionarfloat(4.69875f);
        vetores.adicionarfloat(3.1415936f);
        vetores.adicionarfloat(3.534f);
        vetores.mostrarfloat();
        System.out.println("Tamanho:" + vetores.tamanhofloat);
        System.out.println("--------------------------");
        vetores.removefloat(3);
        vetores.mostrarfloat();
        System.out.println("Tamanho:" + vetores.tamanhofloat);
        System.out.println("--------------------------");
        vetores.removenullfloat(3);
        vetores.mostrarfloat();
        System.out.println("Tamanho:" + vetores.tamanhofloat);
        System.out.println("--------------------------");
    }
}
