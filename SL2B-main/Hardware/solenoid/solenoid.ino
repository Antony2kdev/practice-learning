int solenoid = 3;
int led = 13;
//100111
char seq[7] = "000000";
char data;
void setup() {
  // put your setup code here, to run once:
  pinMode(12,OUTPUT);
}

void loop() {
 
  Serial.begin(9600);
  char data[7] = "000000";
  int length = Serial.readBytesUntil('\n',data,6);

  if(length==6){
    Serial.print("\n");
    Serial.print(data);
  }
  for(int i=0;i<=5;i++){
    seq[i] = data[i];
  }
  for(int i=0;i<=5;i++){
    if(seq[i]=='0'){
    digitalWrite(3+i,LOW);
    }else{
     digitalWrite(3+i,HIGH);
    }
  }
  delay(5000);
  for(int i=0;i<=3;i++){
    digitalWrite(3+i,LOW);
  } 
  // digitalWrite(12,HIGH);

}
