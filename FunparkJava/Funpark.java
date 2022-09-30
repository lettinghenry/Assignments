import java.util.Scanner;
import java.io.*;
import java.util.*;
import java.text.SimpleDateFormat;

public class Funpark {

    public static ArrayList<Ticket> ticketList = new ArrayList<Ticket>();

    public static void main(String args[]) {

        displayMenu();

    }

    /*
     * Display menu
     */
    static public void displayMenu() {
        System.out.println(
                "\nSelect Option to Start.\n1. Enter new E-Ticket" + "\n"
                        + "2. Display Summary of Purchases" + "\n"
                        + "3. Display Summary of Purchases for Selected Month" + "\n"
                        + "4. Find and display customer" + "\n"
                        + "0. Exit");
        processUserInput();
    }

    /**
     * prompt user for input and process
     */
    static public void processUserInput() {
        Scanner sc = new Scanner(System.in);
        try {
            int input = sc.nextInt();
            System.out.println("\nYour selection: " + input+"\n");
            switch (input) {
                case 1:
                    execute1();
                    break;
                case 2:
                    execute2();
                    break;
                case 3:
                    execute3();
                    break;
                case 4:
                    execute4();
                    break;
                case 0:
                    execute0();
                    break;
                default:
                    System.out.println("Please make a valid selection.");
                    displayMenu();
                    break;
            }
        } catch (InputMismatchException ime) {
            System.out.println("Please input number e.g 1, 2, 3 etc");
            processUserInput();
        }
    }

    /**
     * read input file
     * 
     * @param pathToFile
     * @return list of records ArrayList<Ticket>
     */
    public static ArrayList<Ticket> readFile(String pathToFile) {
        try {
            File file = new File(pathToFile);
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String line = "";
            String[] tempArr;
            String delimiter = ",";
            ArrayList<Ticket> ticketList = new ArrayList<>();
            while ((line = br.readLine()) != null) {
                tempArr = line.split(delimiter);
                // save ticket details
                Ticket ticket = new Ticket(tempArr[0], tempArr[1], tempArr[2], tempArr[3], tempArr[4], tempArr[5]);
                ticketList.add(ticket);// add to list
                // for (int i = 0; i < tempArr.length; i++) {
                // // System.out.print(tempArr[i] + " ");
                // }
                // System.out.println();
            }
            br.close();
        } catch (IOException ioe) {
            System.out.println("Something went wrong while opening the file. Check if file exists.");
        }
        return ticketList;
    }

    /**
     * function to update ticket records file
     */
    public static void writeTicketToFile(String filename, String text) {

        try (FileWriter fw = new FileWriter(filename, true);
                BufferedWriter bw = new BufferedWriter(fw);
                PrintWriter out = new PrintWriter(bw)) {
            out.println(text);

        } catch (IOException e) {
            System.out.println("Something went wrong while writing to the file. Check if file exists and naming.");
        }
    }

    /**
     * Function to format and display summary of purchases
     * 
     * @param filename
     * @param totalTickets
     * @param averageTicketPrice
     * @param climbingTot
     * @param trampoliningTot
     * @param waterSlTot
     * @param mnthVals
     */
    public static void displaySummaryOfPurchases(String filename, String totalTickets,
            String averageTicketPrice, String climbingTot, String trampoliningTot,
            String waterSlTot, String[] mnthVals) {

        String summary = "Summary of File: " + filename + "\n" +
                "Total tickets purchased: " + totalTickets + "\n" +
                "Average ticket price: " + averageTicketPrice + "\n\n" +
                "Tickets purchased per activity:\n" +
                "Climbing Wall: " + climbingTot + "\n" +
                "Trampolining: " + trampoliningTot + "\n" +
                "Water Slides: " + waterSlTot + "\n";

        String monthNames = String.format("%-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s",
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec");
        String monthValues = String.format("%-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s %-3s",
                mnthVals[0], mnthVals[1], mnthVals[2], mnthVals[3], mnthVals[4], mnthVals[5],
                mnthVals[6], mnthVals[7], mnthVals[8], mnthVals[9], mnthVals[10], mnthVals[11]);

        System.out.println(summary + "\n" + monthNames + "\n" + monthValues);

    }

    /**
     * Function to format and display monthly summary of purchases
     * 
     * @param filename
     * @param monthName
     * @param totalTickets
     * @param averageTicketPrice
     * @param climbingTot
     * @param trampoliningTot
     * @param waterSlTot
     * @param mnthVals
     */
    public static void displayMonthlySummaryOfPurchases(String filename, String monthName, String totalTickets,
            String averageTicketPrice, String climbingTot, String trampoliningTot,
            String waterSlTot, String[] mnthVals) {

        String summary = "Summary of File: " + filename + "\n" +
                "Total tickets purchased in " + monthName + ": " + totalTickets + "\n" +
                "Average ticket price: " + averageTicketPrice + "\n\n" +
                "Tickets purchased per activity:\n" +
                "Climbing Wall: " + climbingTot + "\n" +
                "Trampolining: " + trampoliningTot + "\n" +
                "Water Slides: " + waterSlTot + "\n";

        System.out.println(summary);

    }

    /**
     * function to display tickets for specific customer
     * 
     * @param ticketList
     */
    public static void displayTickets(List<Ticket> ticketList) {

        for (Ticket ticket : ticketList) {
            System.out.println(ticket.toString());
        }

    }

    /**
     * Menu Option 1
     */
    static public void execute1() {

        String date = getDate();

        Scanner sc;
        System.out.println("Input customer's Name.");
        sc = new Scanner(System.in);
        String name = sc.nextLine();

        System.out.println("Input Activity 1 ('C','T' or 'W')");
        sc = new Scanner(System.in);
        String activity1 = sc.nextLine();

        System.out.println("Input Activity 2 ('C','T','W' or '0')");
        sc = new Scanner(System.in);
        String activity2 = sc.nextLine();

        System.out.println("Input Activity 3 ('C','T','W' or '0')");
        sc = new Scanner(System.in);
        String activity3 = sc.nextLine();

        Ticket ticket = new Ticket(date, activity1, activity2, activity3, "TODO", name);

        String displayString = ticket.toString();
        writeTicketToFile("tickets2022.txt", ticket.printString);// write ticket to file
        System.out.println(displayString); // print ticket details

        // display menu again
        displayMenu();
    }

    /**
     * 
     * @return ticketsList
     */
    static public ArrayList<Ticket> userSelectFile() {

        Scanner sc;
        System.out.println("Select option\n1.Last Year's\n2.New\n");
        sc = new Scanner(System.in);
        String selection = sc.nextLine();
        if (!selection.equalsIgnoreCase("1") && !selection.equalsIgnoreCase("2")) {
            System.out.println("Please enter '1' or '2'");
            execute2();
        }

        ArrayList<Ticket> ticketList = selection.equalsIgnoreCase("1") ? readFile("tickets2021.txt")
                : readFile("tickets2022.txt");

        return ticketList;

    }

    /**
     * Menu Option 2
     */
    static public void execute2() {
        userSelectFile();
        //TODO
        displayMenu();
    }

    /**
     * Menu Option 3
     */
    static public void execute3() {
        userSelectFile();
        //TODO
        displayMenu();
    }

    /**
     * Menu Option 4
     */
    static public void execute4() {
        userSelectFile();
        //TODO
        displayMenu();
    }

    /**
     * Menu Option 5
     */
    static public void execute0() {
        System.out.println("Exiting Program.\nBye :)");
    }

    /**
     * get date
     * 
     * @return date string
     */
    public static String getDate() {
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("dd-MMM-yyyy");
        return sdf.format(cal.getTime());
    }

}

class Ticket {

    static int climbingPrice = 10;
    static int trampoliningPrice = 12;
    static int waterSlidesPrice = 15;
    String printString = "";

    String date = "", f1 = "", f2 = "", f3 = "", number = "", name = "";

    Ticket(String date, String f1, String f2, String f3, String number, String name) {
        this.f1 = f1;
        this.f2 = f2;
        this.f3 = f3;
        this.date = date;
        this.number = number;
        this.name = name;
    }

    /**
     * function to match letter with numeric value
     * 
     * @param activityValue
     * @return activityprice
     */
    public int getActivityPrice(String activityValue) {

        activityValue = activityValue + "";// sanitize
        if (activityValue.equalsIgnoreCase("c")) {
            return climbingPrice;
        } else if (activityValue.equalsIgnoreCase("t")) {
            return trampoliningPrice;
        } else if (activityValue.equalsIgnoreCase("w")) {
            return waterSlidesPrice;
        } else {
            return 0;
        }
    }

    /**
     * get full name of activity given initials.
     * 
     * @param activityValue
     * @return fullname
     */
    public String getActivityFullname(String activityValue) {

        activityValue = activityValue + "";// sanitize
        if (activityValue.equalsIgnoreCase("c")) {
            return "Climbing Wall";
        } else if (activityValue.equalsIgnoreCase("t")) {
            return "Trampolining";
        } else if (activityValue.equalsIgnoreCase("w")) {
            return "Water Slides ";
        } else {
            return "";
        }
    }

    /**
     * function to return total after applying discount
     * 
     * @return
     */
    public double calculateTotalAfterDiscount() {

        int total = getActivityPrice(this.f1) + getActivityPrice(this.f2) + getActivityPrice(this.f3);
        double totalAfterDiscount = total - (getDiscount() * total);

        return totalAfterDiscount;
    }

    /**
     * get discount based on activities selected
     * 
     * @return discount rate
     */
    public double getDiscount() {

        double discount = 0;
        boolean f2IsEmpty = this.f2.equalsIgnoreCase("0");
        boolean f3IsEmpty = this.f3.equalsIgnoreCase("0");

        if (!f2IsEmpty && !f3IsEmpty) {
            discount = 0.2;
        } else {
            discount = 0.1;
        }

        return discount;
    }

    /**
     * convert object to string
     */
    public String toString() {

        double discount = getDiscount();
        String discountPercent = String.valueOf(discount * 100);
        String priceIncludingDiscount = String.format("£%.2f ", calculateTotalAfterDiscount() / 100);
        String discountString = discount > 0 ? "Discount: " + discountPercent : "";

        String displayString = "Customer: " + this.name + "\n"
                + "Date: " + this.date + "              " + discountString + "\n"
                + "Activity 1: " + getActivityFullname(this.f1) + "\n"
                + "Activity 2: " + getActivityFullname(this.f2) + "\n"
                + "Activity 3: " + getActivityFullname(this.f3) + "\n"
                + "Price including discount: " + priceIncludingDiscount + "\n";

        this.printString = this.date + ","
                + this.f1.toUpperCase() + ","
                + this.f2.toUpperCase() + ","
                + this.f3.toUpperCase() + ","
                + this.number + ","
                + this.name;

        return displayString;
    }

}
