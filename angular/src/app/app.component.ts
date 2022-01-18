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
  constructor(private RestService: RestService) {

  }
  ngOnInit(): void {
    this.cargarData();
  }

  public cargarData() {
    this.RestService.get('http://localhost:8000/api/personajes/')
      .subscribe(respuesta => {
        this.listaPj = respuesta;
        console.log("load respuesta: ");
        console.log(this.listaPj);
      })
  }
}
