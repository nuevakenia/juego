import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetallepjComponent } from './detallepj.component';

describe('DetallepjComponent', () => {
  let component: DetallepjComponent;
  let fixture: ComponentFixture<DetallepjComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetallepjComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DetallepjComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
