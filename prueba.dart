void main() {
 int a = 5;
 int b = 5;
 int suma;
 bool activado = null;
suma = a + b;
 
  if(suma >= 10){
    activado = true;
  } else {
    activado = false;
  }
print(activado);
 if( activado == true ){
   print('Activado');
 }else{
   print('Desactivado');
 }
}