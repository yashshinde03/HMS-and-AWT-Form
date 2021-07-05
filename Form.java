package com.company;



import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Form {
    Form() {
        Frame fr = new Frame("Student Form");
        fr.setLayout(null);
        fr.setSize(800, 800);
        fr.setVisible(true);
        Label lb1 = new Label("Name : ");
        lb1.setBounds(20, 20, 50, 50);
        fr.add(lb1);
        TextField tf1 = new TextField();

        Label lb2 = new Label("DOB : ");
        lb2.setBounds(20,77,50,30);
        fr.add(lb2);
        tf1.setBounds(90, 38, 100, 25);
        fr.add(tf1);
        TextField tf2 = new TextField();
        tf2.setBounds(90,88,100,25);
        fr.add(tf2);
        Label lb3 = new Label("Address : ");
        lb3.setBounds(20,127,50,30);
        fr.add(lb3);
        TextField tf3 = new TextField();
        tf3.setBounds(90,138,100,25);
        fr.add(tf3);
        fr.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
//                dispose();//It will help us to close are GUI by clicking X- button
                Frame fr = (Frame) e.getSource();
                fr.dispose();
            }
        });
        Label lb4 = new Label("Class : ");
        lb4.setBounds(20,178,50,30);
        fr.add(lb4);
        // Choices it will add dropdown
        Choice c = new Choice();
        c.setBounds(90,188,100,25);
        c.add("1st");
        c.add("2nd");
        c.add("3rd");
        c.add("4th");
        c.add("5th");
        c.add("6th");
        c.add("7th");
        c.add("8th");
        c.add("9th");
        c.add("10th");
        c.add("11th");
        c.add("12th");
        fr.add(c);
        Label lb5 = new Label("PhoneNo.:");
        lb5.setBounds(20,228,57,30);
        fr.add(lb5);
        TextField tf5 = new TextField();
        tf5.setBounds(90,238,100,25);
        fr.add(tf5);
        Label lb6 = new Label("Gender : ");
        lb6.setBounds(20,278,50,30);
        fr.add(lb6);
        Checkbox cb1 = new Checkbox("Male",true);
        cb1.setBounds(90,284,100,25);
        fr.add(cb1);
        Checkbox cb2= new Checkbox("Female");
        cb2.setBounds(200,284,100,25);
        fr.add(cb2);
        Button b = new Button("Submit");
        b.setBounds(20,384,100,25);
        fr.add(b);

    }





    public static void main(String[] args) {
        Form fo = new Form();
    }
}
