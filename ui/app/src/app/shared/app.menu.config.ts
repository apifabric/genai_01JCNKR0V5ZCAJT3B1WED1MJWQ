import { MenuRootItem } from 'ontimize-web-ngx';

import { ActivityCardComponent } from './Activity-card/Activity-card.component';

import { AirportCardComponent } from './Airport-card/Airport-card.component';

import { BookingCardComponent } from './Booking-card/Booking-card.component';

import { FlightCardComponent } from './Flight-card/Flight-card.component';

import { HolidayCardComponent } from './Holiday-card/Holiday-card.component';

import { PassengerCardComponent } from './Passenger-card/Passenger-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { UserCardComponent } from './User-card/User-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Activity', name: 'ACTIVITY', icon: 'view_list', route: '/main/Activity' }
    
        ,{ id: 'Airport', name: 'AIRPORT', icon: 'view_list', route: '/main/Airport' }
    
        ,{ id: 'Booking', name: 'BOOKING', icon: 'view_list', route: '/main/Booking' }
    
        ,{ id: 'Flight', name: 'FLIGHT', icon: 'view_list', route: '/main/Flight' }
    
        ,{ id: 'Holiday', name: 'HOLIDAY', icon: 'view_list', route: '/main/Holiday' }
    
        ,{ id: 'Passenger', name: 'PASSENGER', icon: 'view_list', route: '/main/Passenger' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'User', name: 'USER', icon: 'view_list', route: '/main/User' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    ActivityCardComponent

    ,AirportCardComponent

    ,BookingCardComponent

    ,FlightCardComponent

    ,HolidayCardComponent

    ,PassengerCardComponent

    ,ReviewCardComponent

    ,UserCardComponent

];