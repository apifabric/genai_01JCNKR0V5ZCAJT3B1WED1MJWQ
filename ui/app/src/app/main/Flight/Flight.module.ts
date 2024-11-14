import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {FLIGHT_MODULE_DECLARATIONS, FlightRoutingModule} from  './Flight-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    FlightRoutingModule
  ],
  declarations: FLIGHT_MODULE_DECLARATIONS,
  exports: FLIGHT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class FlightModule { }