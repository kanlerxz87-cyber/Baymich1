const MICHELIN_2026 = 'https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california';
// The entries and star levels below are transcribed from Michelin's 2026 California article.
// The article exposes direct restaurant profile links for every included starred entry.
const restaurants = [
  {name:'Atelier Crenn',city:'San Francisco',stars:3,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/atelier-crenn',officialUrl:'https://www.ateliercrenn.com/',socials:[{label:'Instagram',url:'https://www.instagram.com/atelier.crenn/',source:'Official Atelier Crenn site'}]},
  {name:'Benu',city:'San Francisco',stars:3,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/benu'},
  {name:'Californios',city:'San Francisco',stars:3,url:'https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios'},
  {name:'Quince',city:'San Francisco',stars:3,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/quince'},
  {name:'SingleThread',city:'Healdsburg',stars:3,url:'https://guide.michelin.com/ca/en/california/healdsburg/restaurant/singlethread'},
  {name:'Enclos',city:'Sonoma',stars:3,url:'https://guide.michelin.com/ca/en/california/sonoma/restaurant/enclos',newIn2026:true},
  {name:'The French Laundry',city:'Yountville',stars:3,url:'https://guide.michelin.com/ca/en/california/yountville/restaurant/the-french-laundry'},
  {name:'Acquerello',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/acquerello'},
  {name:'Birdsong',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/birdsong'},
  {name:'Kiln',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/kiln-1210355'},
  {name:'Lazy Bear',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/lazy-bear'},
  {name:'Saison',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/saison'},
  {name:'Sons & Daughters',city:'San Francisco',stars:2,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/sons-daughters'},
  {name:'Commis',city:'Oakland',stars:2,url:'https://guide.michelin.com/ca/en/california/oakland/restaurant/commis',officialUrl:'https://commisrestaurant.com/info/',priceText:'$669.60 for two before tax and beverages (10-course menu $279/person + 20% service charge; published menu arithmetic)',priceUrl:'https://commisrestaurant.com/info/'},
  {name:'Selby’s',city:'Atherton',stars:1,url:'https://guide.michelin.com/ca/en/california/atherton/restaurant/selby-s'},
  {name:'Auro',city:'Calistoga',stars:1,url:'https://guide.michelin.com/ca/en/california/calistoga/restaurant/auro'},
  {name:'Cyrus',city:'Geyserville',stars:1,url:'https://guide.michelin.com/ca/en/california/geyserville/restaurant/cyrus'},
  {name:'Sun Moon Studio',city:'Oakland',stars:1,url:'https://guide.michelin.com/ca/en/california/oakland/restaurant/sun-moon-studio'},
  {name:'Protégé',city:'Palo Alto',stars:1,url:'https://guide.michelin.com/ca/en/california/palo-alto/restaurant/protege'},
  {name:'Auberge du Soleil',city:'Rutherford',stars:1,url:'https://guide.michelin.com/ca/en/california/rutherford/restaurant/auberge-du-soleil'},
  {name:'Press',city:'Saint Helena',stars:1,url:'https://guide.michelin.com/ca/en/california/saint-helena/restaurant/press'},
  {name:'Madcap',city:'San Anselmo',stars:1,url:'https://guide.michelin.com/ca/en/california/san-anselmo/restaurant/madcap'},
  {name:'7 Adams',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/7-adams'},
  {name:'Angler SF',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/angler-sf'},
  {name:'Hilda and Jesse',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/hilda-and-jesse'},
  {name:'Kin Khao',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/kin-khao'},
  {name:'Mister Jiu’s',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/mister-jiu%E2%80%99s'},
  {name:'Naides',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/naides',newIn2026:true},
  {name:'Nari',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/nari'},
  {name:'Niku Steakhouse',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/niku-steakhouse'},
  {name:'Nisei',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/nisei'},
  {name:'San Ho Won',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/san-ho-won'},
  {name:'Sorrel',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/sorrel'},
  {name:'Ssal',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/ssal'},
  {name:'State Bird Provisions',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/state-bird-provisions'},
  {name:'The Progress',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/the-progress'},
  {name:'Wolfsbane',city:'San Francisco',stars:1,url:'https://guide.michelin.com/ca/en/california/san-francisco/restaurant/wolfsbane',newIn2026:true},
  {name:'Wakuriya',city:'San Mateo',stars:1,url:'https://guide.michelin.com/ca/en/california/san-mateo/restaurant/wakuriya'},
  {name:'The Village Pub',city:'Woodside',stars:1,url:'https://guide.michelin.com/ca/en/california/woodside/restaurant/the-village-pub'},
  {name:'Maria Isabel',city:'San Francisco',stars:0,label:'Guide Recommended',url:'https://guide.michelin.com/us/en/california/san-francisco/restaurant/maria-isabel',note:'Michelin describes this as a Recommended restaurant in its 2026 article; no star is shown there.'}
];

const areaGroups = [
  {name:'San Francisco',cities:['San Francisco'],mapLabel:'Michelin-starred restaurants in San Francisco'},
  {name:'East Bay',cities:['Oakland'],mapLabel:'Michelin-starred restaurants in Oakland, California'},
  {name:'Peninsula & South Bay',cities:['Atherton','Palo Alto','San Mateo','Woodside'],mapLabel:'Michelin-starred restaurants on the San Francisco Peninsula'},
  {name:'Wine Country',cities:['Calistoga','Geyserville','Healdsburg','Rutherford','Saint Helena','Sonoma','Yountville'],mapLabel:'Michelin-starred restaurants in Napa and Sonoma County'},
  {name:'Marin County',cities:['San Anselmo'],mapLabel:'Michelin-starred restaurants in Marin County'}
];
