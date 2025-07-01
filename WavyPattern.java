public class WavyPattern {
    public static void main(String[] args) throws InterruptedException {
        for (int row = 0; row < 20; row++) 
            for (int col = 0; col < 80; col++) {
                if (Math.sin((col + row) * 0.2) > 0.8)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
            Thread.sleep(100); // delay for wave motion
        }

        System.out.println("\u001B[31mRed Text\u001B[0m");

        
    }
}
