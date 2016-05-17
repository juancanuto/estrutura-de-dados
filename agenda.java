
import java.util.LinkedList;

public class Agenda {
    
   
    
    private int id;
    private String nome;
    private int idade;
    private float altura;
    private LinkedList <Agenda> pessoas;
    
    public Agenda(String nome, int idade, float altura){
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;	
    	    }
   
	public void armazenaPessoas(String nome, int idade , float altura){
		Agenda pessoa = new Agenda(nome, idade, altura);
				pessoas.add(pessoa);
	}
	
	public void removePessoa(String nome){
		for (Agenda pessoa : this.pessoas){
			if (pessoa.nome == nome){
			    pessoas.remove(pessoa);
			}
		}
		
	}	    
			    
	public int buscaPessoa(String nome){
		int index = 0;
		for (Agenda pessoa : this.pessoas){
			index = pessoas.indexOf(pessoa);
		}
		return index;
	}
	
	public void imprimeAgenda(){
		for(Agenda pessoa : pessoas){
			System.out.println(pessoa);
		}
	}
	
	public void imprimePessoas(int index){
		for (Agenda pessoa : this.pessoas)
			System.out.println(pessoas.get(index));
		
	}
}
