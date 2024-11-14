import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {HOLIDAY_MODULE_DECLARATIONS, HolidayRoutingModule} from  './Holiday-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    HolidayRoutingModule
  ],
  declarations: HOLIDAY_MODULE_DECLARATIONS,
  exports: HOLIDAY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class HolidayModule { }