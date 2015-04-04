import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.*;
//importjava.net.MalformedURLException;
import de.l3s.boilerpipe.extractors.DefaultExtractor;
public class Trial {
    public static void main(String[] args) throws Exception, IOException {
        
            BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\HP\\Desktop\\10k.txt"));
        String l;
           BufferedWriter bw = new BufferedWriter(new FileWriter("C:\\Users\\HP\\Desktop\\boilerpipe1.txt"));
           int i =0;
           while((l=br.readLine())!= null)
            {
             try{
             final URL url = new URL(l);
             
             bw.write(DefaultExtractor.INSTANCE.getText(url));
             i= i+1;
             System.out.println("The value of i is " + i + " URL:" + url);
             //System.out.println(DefaultExtractor.INSTANCE.getText(url));          
}catch (Exception ex)
{
System.out.println(ex);
}
}
bw.close();
} 
    }