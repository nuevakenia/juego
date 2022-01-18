import { Component, OnInit, Input } from '@angular/core';
import { products } from '../products';

@Component({
  selector: 'app-seleccion-personaje',
  templateUrl: './seleccion-personaje.component.html',
  styleUrls: ['./seleccion-personaje.component.css']
})
export class SeleccionPersonajeComponent implements OnInit {

  products = products;
  @Input() personajes = [
    {
      nombre: 'Phone XL'
    },
    {
      nombre: 'Phone Mini'
    },
    {
      nombre: 'Phone Standard'
    }
  ];


  share() {
    window.alert('The product has been shared!');
  }

  constructor() { }

  ngOnInit(): void {
  }

}
