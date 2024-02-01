/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package carmanager;

/**
 *
 * @author ADMIN
 */
class Car {
    private String Colour;
    private int EnginePower;
    private boolean Convertible;
    private boolean ParkingBrake;
    public Car(){
    
}
    public Car(String Colour, int EnginePower, boolean Convertible, boolean ParkingBrake){
        this.Colour = Colour;
        this.Convertible = Convertible;
        this.EnginePower = EnginePower;
        this.ParkingBrake = ParkingBrake;
    }

    public String getColour() {
        return Colour;
    }

    public void setColour(String Colour) {
        this.Colour = Colour;
    }

    public int getEnginePower() {
        return EnginePower;
    }

    public void setEnginePower(int EnginePower) {
        this.EnginePower = EnginePower;
    }

    public boolean isConvertible() {
        return Convertible;
    }

    public void setConvertible(boolean Convertible) {
        this.Convertible = Convertible;
    }

    public boolean isParkingBrake() {
        return ParkingBrake;
    }

    public void setParkingBrake(boolean ParkingBrake) {
        this.ParkingBrake = ParkingBrake;
    }
    void pressStartButton(){
        System.out.println("You have pressed the start button");
    }
    void pressAcceleratorButton(){
        System.out.println("You have pressed the Accelerator button");
    }

    public String output() {
        return "Car{" + "Colour=" + Colour + ", EnginePower=" + EnginePower + ", Convertible=" + Convertible + ", ParkingBrake=" + ParkingBrake + '}';
    }
    
}
