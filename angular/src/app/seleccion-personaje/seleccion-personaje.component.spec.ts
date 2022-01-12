import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeleccionPersonajeComponent } from './seleccion-personaje.component';

describe('SeleccionPersonajeComponent', () => {
  let component: SeleccionPersonajeComponent;
  let fixture: ComponentFixture<SeleccionPersonajeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SeleccionPersonajeComponent]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SeleccionPersonajeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
