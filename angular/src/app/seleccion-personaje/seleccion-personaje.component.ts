import { Component, OnInit, Input, HostBinding } from '@angular/core';
import { products } from '../products';

//Anim
import {
  trigger,
  state,
  style,
  animate,
  transition
} from '@angular/animations';

@Component({
  selector: 'app-seleccion-personaje',
  templateUrl: './seleccion-personaje.component.html',
  styleUrls: ['./seleccion-personaje.component.css'],
  animations: [
    trigger('selectorPj', [
      state('activo', style({
        height: '100px',
        opacity: 1
      })),

      state('inactivo', style({
        height: '100px',
        opacity: 0.5,
        backgroundColor: 'gray'
      })),

      transition('activo => inactivo', [
        animate('1s')
      ]),
      transition('inactivo => activo', [
        animate('0.5s')
      ])
    ])
  ]
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
  // Selector pj
  isSelected = true;

  toggleIzq() {
    this.isSelected = !this.isSelected;
  }
  toggleDer() {
    this.isSelected = !this.isSelected;
  }
  toggleCentro() {
    this.isSelected = !this.isSelected;
  }


  share() {
    window.alert('The product has been shared!');
  }

  constructor() { }

  ngOnInit(): void {
  }

}

