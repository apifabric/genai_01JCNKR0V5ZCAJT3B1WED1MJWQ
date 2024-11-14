import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PASSENGER_MODULE_DECLARATIONS, PassengerRoutingModule} from  './Passenger-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    PassengerRoutingModule
  ],
  declarations: PASSENGER_MODULE_DECLARATIONS,
  exports: PASSENGER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PassengerModule { }