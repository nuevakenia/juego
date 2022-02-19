import { Component, Input } from '@angular/core';
import { RestService } from './rest.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular';

  public listaPj: any = [];
  public creaPj: any = [];
  public detallePj: any = [];

  constructor(private RestService: RestService) {

  }
  ngOnInit(): void {
    this.cargarData();
    this.crearPj();
    this.listarPj();
  }

  public cargarData() {
    this.RestService.get('http://localhost:8000/api/personajes/')
      .subscribe(respuesta => {
        this.listaPj = respuesta;
        console.log("load respuesta: ");
        console.log(this.listaPj);
      })
  }

  public crearPj() {
    this.RestService.get('http://localhost:8000/api/personajes/crear')
      .subscribe(respuesta => {
        this.creaPj = respuesta;
        console.log("Crear PJ: ");
        console.log(this.creaPj);
      })
  }
  
  public listarPj() {
    this.RestService.get('http://localhost:8000/api/personajes/detalle')
      .subscribe(respuesta => {
        this.detallePj = respuesta;
        console.log("Crear PJ: ");
        console.log(this.detallePj);
      })
  }
}
