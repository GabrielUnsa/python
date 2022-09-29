import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import javax.swing.JFileChooser;

public class ThreeSum {
	public static int count(ArrayList<Integer> a){
		int N = a.size();
		int cnt = 0;
		for( int i = 0; i < N; i++)
			for( int j = i+1; j < N; j++)
				for( int k = j+1; k < N; k++)
					if( (int)a.get(i) + (int)a.get(j) + (int)a.get(k) == 0) cnt++;
		return cnt;
	}
	
	public static int SortAnalysis(ArrayList<Integer> a){
		int cnt = 0;
		int N = a.size();
		int j,v;
		boolean b;
		for( int i = 1; i < N; i++){
			v = (int) a.get(i);
			j = i-1;
			b = true;
//			while( j >= 0 && ((int)a.get(j)) > v){
//			cnt++; //Estaria mal aqui el contador porq no cuenta lo que ocurre cuando la condicon es falsa.
//			a.set(j+1,a.get(j));
//			j--;
//			}
			while( j >= 0 && b){	
				cnt ++; //cada vez que entro hago una comparacion y de ser cierta ejecuto el intercambio 
				if( ((int)a.get(j)) > v ){
					a.set(j+1,a.get(j));
					j--;
				} else b = false;
			}
			a.set(j+1,v);
		}
		return cnt;
	}
	
	public static void muestra(ArrayList<Integer> a){
		for(int k = 0; k < a.size(); k++) System.out.println(a.get(k));;
	}
	
	public static void escribir(ArrayList<Integer> a){
		String name="";
		JFileChooser file = new JFileChooser();
		file.showSaveDialog(null);
		File guardado = file.getSelectedFile();
		FileWriter save;
		FileWriter save2;
		try {
			save = new FileWriter(guardado+"OrdDesc.txt");
			BufferedWriter b= new BufferedWriter(save);
			for (int i = 0; i< a.size(); i++){
				b.write(String.valueOf(a.get(i)));
				b.newLine();
			}
			b.close();
			save2 = new FileWriter(guardado+"OrdAsc.txt");
			BufferedWriter br= new BufferedWriter(save2);
			for (int i = a.size()-1; i >= 0; i--){
				br.write(String.valueOf(a.get(i)));
				br.newLine();
			}
			br.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		
	}
	
	public static void main (String[] args){
		ArrayList<Integer> a = new ArrayList<Integer>();
		File archivo = null;
		FileReader fr = null;	
		BufferedReader br =null;
		long startTime = System.currentTimeMillis();
		try{
			archivo = new File ("/home/gabriel/UNSa_2018/TC3/TP2/DatosEjercicioNro1/8Kints.txt");
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);
			String linea;
			while( (linea = br.readLine()) != null){
				while(linea.substring(0,1).compareTo(" ")==0){
					linea=linea.substring(1,linea.length());
				}
				a.add(Integer.parseInt(linea));
			}
		}catch(Exception e){
			e.printStackTrace();
		}finally{
			try{
				if ( null != fr) {
					fr.close();
				}
			}catch(Exception e2){
				e2.printStackTrace();
			}
		}
		System.out.println(SortAnalysis(a));
		System.out.println(System.currentTimeMillis()-startTime + " ms");
	}
}
