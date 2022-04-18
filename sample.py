"""
DATA in TRACK

1. name
2. artist
3. preview url
4. popularity
5. image_url

* These are all stored in a dictionary
** Tracks provided in array

"""

playlist = [
    {
        'name': 'Up All Night (feat. Afrojack)',
        'artists': [
            'VINAI',
            'Hard Lights',
            'Afrojack'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/e4bbb48c7b5318add989829854cd5972560955cc?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 66,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02848b73a862107e28cbc64ebd',
            'width': 300
        }
    },
    {
        'name': 'Purple Lamborghini (with Rick Ross)',
        'artists': [
            'Skrillex',
            'Rick Ross'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/15f9ba1b6b400abfbd6bbb7b049fb60676fee81a?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 71,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02602b6507f5289db71603c2f4',
            'width': 300
        }
    },
    {
        'name': 'Fight Back',
        'artists': [
            'NEFFEX'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8bd0cb83966a2037b5920a3bfadb9b57a8c67d15?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 79,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02bd9e9490d5198c41cb85b669',
            'width': 300
        }
    },
    {
        'name': 'No Glory (feat. M.I.M.E & Drama B)',
        'artists': [
            'Skan',
            'Krale',
            'M.I.M.E',
            'Drama B'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/5783e0913c1e5c378faf8cea92fb411186f6e589?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 66,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e024cc608d65bc5f779b0f9c149',
            'width': 300
        }
    },
    {
        'name': 'Creep - mint Singles',
        'artists': [
            'R3HAB',
            'GATTÜSO'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/15911cb70cfe7ef67a79cd4095951ef4a6a83bb9?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 64,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e020501085f912ca8e861aac2a6',
            'width': 300
        }
    },
    {
        'name': 'Bang Your Head - Naeleck & KATFYR Remix',
        'artists': [
            'Fukkk Offf',
            'Naeleck',
            'KATFYR'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/6b96d63674b0ee2c521e0559d1f8accd32d728bb?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 54,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0234289a3c93db5fc4036ca9d8',
            'width': 300
        }
    },
    {
        'name': 'The Wall',
        'artists': [
            'Alok',
            'Sevenn'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f73e54b9c804cb6a7feecb6957bd1833954a3822?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 58,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0248459ed7712193aadacbfaf1',
            'width': 300
        }
    },
    {
        'name': 'Stay',
        'artists': [
            'Naeleck',
            'Jenil',
            'Heon Seo'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8515e01aed9dd95cdea147ff9f3a19fcd4b2dadc?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 65,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ba7d5b0c09e3d7d72ec1c282',
            'width': 300
        }
    },
    {
        'name': 'Boom Boom Pow',
        'artists': [
            'Zafrir',
            'Afrojack'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/e215867d03171e94f36a9490a2d45c17da7926d0?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 62,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02d95a69b6ed77cb639d819064',
            'width': 300
        }
    },
    {
        'name': 'Dark is All I See',
        'artists': [
            'Naeleck',
            'Oddity',
            'Wasiu'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/9b5c9481418cb0f7da2701e16d3f3684b98c04fe?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 55,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0260cc262c0970edfc414df17d',
            'width': 300
        }
    },
    {
        'name': 'Take Me (feat. Gloria Kim)',
        'artists': [
            'Will Sparks',
            'Gloria Kim'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/66aa04683013cad60934f7ee9589b1e63a6812ce?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 63,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e023174ca251d50f77508cd6852',
            'width': 300
        }
    },
    {
        'name': 'Threnody (Bombs Away Remix)',
        'artists': [
            'Naeleck'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/881d48bcb50adb6d3085761ffc211448e0b7675d?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 62,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02924fb5910f77d8d12100716d',
            'width': 300
        }
    },
    {
        'name': "Sweet Child O' Mine",
        'artists': [
            'The FifthGuys',
            'Invisible',
            'The Late Night Project'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/0381c4983b744bd1d61f0e6b96d12b1d38418333?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 56,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e027ccd148cc4b42eba97c9e72e',
            'width': 300
        }
    },
    {
        'name': 'Roses - Imanbek Remix',
        'artists': [
            'SAINt JHN',
            'Imanbek'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/ea6beae040b775bc6c156743b668f5f3ee984c52?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 84,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02b340b496cb7c38d727ff40be',
            'width': 300
        }
    },
    {
        'name': 'Seven Nation Army',
        'artists': [
            'DJ Fluke',
            'Jaki Nelson'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8bad5e30aa7274f6ec9f4a6b55be2ce8c04e7d35?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 66,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e025e7fb32542ad51959c401f3e',
            'width': 300
        }
    },
    {
        'name': 'Highest In The Room',
        'artists': [
            'SCNDL'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/0f629b12d33e6fee88b0b574be02030335989130?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 55,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ef5dd38ee106f24ecadc707c',
            'width': 300
        }
    },
    {
        'name': 'Every Battle',
        'artists': [
            'Hallman'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/d35883b7ece40cccbb68abc2ae75a67e9ba25b42?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 54,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0214dd5a13255c763fb0ac2eee',
            'width': 300
        }
    },
    {
        'name': 'Majesty',
        'artists': [
            'Apashe',
            'Wasiu'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/94638a7231cc3896a2063efa63936864e8bd766c?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 67,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e026e9cba73e17558eabbe6c5b0',
            'width': 300
        }
    },
    {
        'name': 'Red Cup Killa',
        'artists': [
            'Rolls Rollin'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/a4017d9d90a89013ae744478ded699efc4e71797?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 41,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02c247964690291d12a0c39b49',
            'width': 300
        }
    },
    {
        'name': 'This Time (Never Be Alone Again)',
        'artists': [
            'Dada Life'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/647dc3a156023eec068776b4b51b37f036e124cc?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 57,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02a56747d3c015ecfda113da2d',
            'width': 300
        }
    },
    {
        'name': "Don't Be Shy",
        'artists': [
            'Ketafere'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/9ebfc26a527477113a1f689e941ef3be14dbe0c1?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 41,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02b9e66236e056e660911c900f',
            'width': 300
        }
    },
    {
        'name': 'Virtual Gaming - Misfit Remix',
        'artists': [
            'Naeleck',
            'Hige Driver',
            'Misfit'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/6550f4d44694a82d5ab6ac1b6855b841a0a5343b?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 35,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0240b307c0d1ed218b5ec861b6',
            'width': 300
        }
    },
    {
        'name': 'Any Other Way',
        'artists': [
            'Lost Identities',
            'Anna Vellington'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/e93b57f55bbae17f37ca216aea8bd9c66c96b149?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 34,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e022f90c181051550723712d6c9',
            'width': 300
        }
    },
    {
        'name': 'Infinite Ammo',
        'artists': [
            'Le Castle Vania'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/9650368a9d0b0249ed17cc20be54cfbb94b93ed9?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 52,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e022fa427d287327d3381f0d90a',
            'width': 300
        }
    },
    {
        'name': 'On The Run',
        'artists': [
            'Marnik'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/70575f44e13c7bcffe826b392980998375feb270?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 61,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02eae1fa316e655f11b2b0c66b',
            'width': 300
        }
    },
    {
        'name': 'Give it Back',
        'artists': [
            'DJ Fluke'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/15aade748d14201b3f31e295e6bbc5efb93fcf1f?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 52,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0276a1ac7064bc09d180dcd11a',
            'width': 300
        }
    },
    {
        'name': 'Out of Here',
        'artists': [
            'RudeLies'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/89ae3f64840bbb40a9eb8291b16eaceb193654dd?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 48,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0281b9f47eea7540a9007a5542',
            'width': 300
        }
    },
    {
        'name': 'Do Re Mi',
        'artists': [
            'The FifthGuys',
            'NBLM'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/611c3d7a05d77bfff103dcfb3f82ba5345103421?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 54,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0267b36fa3a2bd82c2ee615b58',
            'width': 300
        }
    },
    {
        'name': 'Virtual Gaming - Tokyo Machine Remix',
        'artists': [
            'Naeleck',
            'Hige Driver',
            'Tokyo Machine'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/461020568aed1155c7e51c9b74c7482e50b072f6?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 54,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0276d7141933da2695428a24ec',
            'width': 300
        }
    },
    {
        'name': 'Need U',
        'artists': [
            'Mephi',
            'ZAHIA'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/39f337ac57cd2ea54310427a430263672f6cd9be?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 42,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02a8a0324af1c134631093c1b4',
            'width': 300
        }
    },
    {
        'name': 'Legends Never Die - (Remix)',
        'artists': [
            'League of Legends',
            'Alan Walker',
            'Against The Current',
            'Mako'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f9845a3d81d42cdd88728fb4e1a09a380992348f?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 70,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e021578debc0e6bb047dd20a02b',
            'width': 300
        }
    },
    {
        'name': 'Monody (feat. Laura Brehm)',
        'artists': [
            'TheFatRat',
            'Laura Brehm'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/c8954969282ca55b4bc43b066a25cc1a86dfa621?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 66,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02f0f3a191d7dcaf2b6a8ac86c',
            'width': 300
        }
    },
    {
        'name': 'In My Head',
        'artists': [
            'Virtual Riot',
            'PRXZM'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/faa7c3162b5fc896c42ddf06efd5f21446f6a6af?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 52,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02af45b5354e740510bdeb3314',
            'width': 300
        }
    },
    {
        'name': 'Ohlala',
        'artists': [
            'Pepperjuice'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/922b92e3573627e9fa6bfc280a00246e3f98fb45?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 43,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02b8c4fd0b365f51af603f3f1a',
            'width': 300
        }
    },
    {
        'name': 'Lies',
        'artists': [
            'Player1',
            'Barbara Argyrou'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/fa497d2b11b6e90fb1f3753e2a40b0ec51ff4cc4?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 52,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02eac10a239bba5a7fd86ac655',
            'width': 300
        }
    },
    {
        'name': 'In The Dark',
        'artists': [
            'Vintage Culture',
            'Fancy Inc'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f8e38cc8faf96eea3e61c7a430a002a365dc1741?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 61,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0209490d9da9807383e5582c77',
            'width': 300
        }
    },
    {
        'name': 'Love Lockdown',
        'artists': [
            'R-Cue'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/5ee5af2ece0ebefbf7b43675f617d97abecb7593?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 55,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e027c6fe30b688b593af909183a',
            'width': 300
        }
    },
    {
        'name': 'Everytime We Touch - Hardwell & Maurice West Remix',
        'artists': [
            'Cascada',
            'Hardwell',
            'Maurice West'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/2148e555cf853b71250e296a5a61c65b32d00c31?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 69,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e029dbc5c4d563b38e335d6250d',
            'width': 300
        }
    },
    {
        'name': 'Bonfire',
        'artists': [
            'Knife Party'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/49e24caa1febb3075736b86924ea6fa68de59031?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 64,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02303ae66195b6feba7022698b',
            'width': 300
        }
    },
    {
        'name': 'Take A Sip - Dodge & Fuski Remix',
        'artists': [
            'Naeleck',
            'Ferd',
            'VIKING N3',
            'Dodge & Fuski'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/ab8b880a90383d0c1ab2b6096acc9df3091e63b4?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 54,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/fb8f1e3149814f2175bd8efdc545e2815f57e81d',
            'width': 300
        }
    },
    {
        'name': 'Gold (Stupid Love)',
        'artists': [
            'Excision',
            'ILLENIUM',
            'Shallows'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8fc55d76e826d0328f6caefe7c6701a7d66c26a9?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 56,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e027f1485281a210cedaeab23b6',
            'width': 300
        }
    },
    {
        'name': 'All Is Lost',
        'artists': [
            'Getter',
            'nothing,nowhere.'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/0faf846e6e187d07323d3d1a9bacd3bab0495730?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 39,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02e2a9ce098fbcca00011e8a2c',
            'width': 300
        }
    },
    {
        'name': 'Shelter',
        'artists': [
            'Porter Robinson',
            'Madeon'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/fbe56383919cff9a224166d9fa9fa11357338c6b?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 68,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e020b4df34612f851b639959f9a',
            'width': 300
        }
    },
    {
        'name': 'Disintegration - Dirtyphonics Remix',
        'artists': [
            'Le Castle Vania',
            'Dirtyphonics'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/aa0793523d680e10baa44d18bae9fa282a11a7f8?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 45,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02988fe813e054aea07967a1ed',
            'width': 300
        }
    },
    {
        'name': 'Blah Blah Blah',
        'artists': [
            'Armin van Buuren'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/4149bd30a4a078a99fbc962879692eb65d358be2?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 68,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e023c68bf2b92f49ae6732fc8f1',
            'width': 300
        }
    },
    {
        'name': 'Butterfly',
        'artists': [
            'Marnik',
            'Hard Lights'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/b82efd37f724b73025af0674719cb0878cbe2ff9?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 61,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02a81f7955ff1d2e80626efe67',
            'width': 300
        }
    },
    {
        'name': 'Drop It',
        'artists': [
            'Tujamo',
            'Lukas Vane'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/24fa76e70e7dc0c9d482492581abd33677e0e0e0?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 63,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ec46a9ea28c68db2708a1a44',
            'width': 300
        }
    },
    {
        'name': 'Carnival - Dimitri Vegas & Like Mike Edit',
        'artists': [
            'Timmy Trumpet',
            'MATTN',
            'Wolfpack',
            'X-TOF',
            'Dimitri Vegas & Like Mike'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/06b97b383e5c5324bbaa623d488246d54a993353?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 57,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02836e40ed3e5a6e8f5a94810a',
            'width': 300
        }
    },
    {
        'name': 'The Line Is Bugged',
        'artists': [
            'Cyberpunkers'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/960eb894df75515c434e6c2ad3c02aff2704abab?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 43,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0212a442c389d5cd5b4e3eeb11',
            'width': 300
        }
    },
    {
        'name': 'Back To You',
        'artists': [
            'CASHEW'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/12ca18e278f45fc5bfc3c45e4e083385b8644137?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 44,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02f7fc23bb7ec2481ec7cb5549',
            'width': 300
        }
    },
    {
        'name': 'Virtual Gaming',
        'artists': [
            'Naeleck',
            'Hige Driver'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f887b81869a60a4bf094e56c1fb20d899e01f7e6?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 46,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0247f387632137353fe8376544',
            'width': 300
        }
    },
    {
        'name': 'Death Rattle',
        'artists': [
            'Blanke',
            'REAPER'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/63608e28e2870b15181f70c6c0ac6cb5d254b2c0?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 51,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0234289a3c93db5fc4036ca9d8',
            'width': 300
        }
    },
    {
        'name': 'Vivimus',
        'artists': [
            'Tim Hox',
            'Vessbroz'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8d89b267d6aeaa45cadf3e0b52c322ac04dddb7d?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 43,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e025f02a7f23a9fe2477e1b8dfc',
            'width': 300
        }
    },
    {
        'name': 'The Business',
        'artists': [
            'Tiësto'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/0eab33c8cf88fdd3046bd58133b6cbf2fe31773c?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 87,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02f461bbc21a9bcec43a926973',
            'width': 300
        }
    },
    {
        'name': 'Space Ranger',
        'artists': [
            'MASTAD'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/cd7a7220068ac7577514d89f659c7be7e8629c0c?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 31,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02f0d40cc5328c7889af538991',
            'width': 300
        }
    },
    {
        'name': 'Love Magic',
        'artists': [
            'Bombs Away'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/78e8c176676620c2798c654371fd46f646d79b48?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 39,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e023b4ef9e016157730127ae48a',
            'width': 300
        }
    },
    {
        'name': 'Anything',
        'artists': [
            'Alison Wonderland',
            'Valentino Khan'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/41bd57c7e1676a02ef80b50e0f72c25c99e19966?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 65,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02d58c33753ecbe7e20fde9582',
            'width': 300
        }
    },
    {
        'name': 'IM GONE',
        'artists': [
            'JOYRYDE'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/31e559aeb7b742e116838af9d9d7eba6b232c948?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 46,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02636ec0e3f3f65cf70a4d7ad6',
            'width': 300
        }
    },
    {
        'name': 'Gambetta',
        'artists': [
            'Fatesky',
            'Lodgerz'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/c56cc98f62321c3cb7c0382e07c8b420e8631f49?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 42,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0290f95cc4ef65ae7bde4a3bf6',
            'width': 300
        }
    },
    {
        'name': 'Reality Engine',
        'artists': [
            'Nanoo',
            'Extra Terra'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/3ea05887d49bf7dcfba85110f60d0d7f63a26cca?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 37,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02174b326de04c82529e447b59',
            'width': 300
        }
    },
    {
        'name': 'Fall Into Me (feat. Dylan Matthew)',
        'artists': [
            'NGHTMRE',
            'SLANDER',
            'Dylan Matthew'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/25ad8e1277605f0e4a13b56bef82fdb5bbcda1ba?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 67,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0208c6f5a7b303468ba07429e5',
            'width': 300
        }
    },
    {
        'name': 'Virtual Gaming - A-Dyad Remix',
        'artists': [
            'Naeleck',
            'Hige Driver',
            'A-Dyad'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/38f30f1c9f81c0834e3d969cb7977743b9f5d81a?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 32,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0240b307c0d1ed218b5ec861b6',
            'width': 300
        }
    },
    {
        'name': 'On That Road',
        'artists': [
            'The FifthGuys',
            'BTWRKS',
            'Godmode'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/eff1c2d9502e9a8d643f7addce0a21de4e80ec8e?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 47,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e021de87b459d8098b546845745',
            'width': 300
        }
    },
    {
        'name': 'Playdough',
        'artists': [
            'Biometrix'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/1b6e91da1dd7331055f6a03f8c75b714deee06d5?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 41,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0230f8c764df1114e59b45a680',
            'width': 300
        }
    },
    {
        'name': 'Go Ahead',
        'artists': [
            'Cyberpunkers'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/c033fe616cfbe83fcd7742de7c2433c6a5cafabe?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 43,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0212a442c389d5cd5b4e3eeb11',
            'width': 300
        }
    },
    {
        'name': 'Piranha',
        'artists': [
            'Cartoon',
            'Pluuto'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/4e2a202cdf13b78ec5d3a499ab52d663d7250f28?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 65,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e021cad1e99f2723d7eb905f66a',
            'width': 300
        }
    },
    {
        'name': 'Helicopter (with Jungle Jonsson)',
        'artists': [
            'Hard Lights',
            'Jungle Jonsson'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/9479af6db1503a56c4995619dbc228c47a292bd4?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 57,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0242aabdd7475dedce37f333b4',
            'width': 300
        }
    },
    {
        'name': 'Incredible (feat. Insali)',
        'artists': [
            'Frontliner',
            'Insali'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/ad238dade4f19a426db7ea6097c21462d7a21eca?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 53,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02150d17f0f03a5845be1f5bcc',
            'width': 300
        }
    },
    {
        'name': 'Beast (All as One)',
        'artists': [
            'Dimitri Vegas & Like Mike',
            'Ummet Ozcan',
            'Brennan Heart'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f31f5cc435c70b75906cb147859b0eb4c7684d5e?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 63,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ffe0e0c612d1f4ce6f3761a3',
            'width': 300
        }
    },
    {
        'name': 'STFU',
        'artists': [
            'SPECT3R'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/2a4c006bca43131fe46324cda5277d64245564b1?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 37,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0228869673ac6784a0fc60ddb5',
            'width': 300
        }
    },
    {
        'name': 'The Wailing',
        'artists': [
            'Tomatow',
            'Nadya Sumarsono'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/28f029615530d0f37c40efb5639b71a457430972?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 22,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0228d5a35dddcef58adc7c81d9',
            'width': 300
        }
    },
    {
        'name': 'No Parallels',
        'artists': [
            'Victor Tellagio',
            'Sodda',
            'Armen Paul'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/18c794cc4fd078d40de350742f76b37b1348dc48?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 34,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0239360f5fe7db8b2075acba7c',
            'width': 300
        }
    },
    {
        'name': 'Get in Trouble (So What)',
        'artists': [
            'Dimitri Vegas & Like Mike',
            'Vini Vici',
            'Dimitri Vegas'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/a0258c294a8b9735882f00d485931df99fdb7c48?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 65,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02637c265de6e5223aeda8b5ee',
            'width': 300
        }
    },
    {
        'name': 'Arcade',
        'artists': [
            'The FifthGuys',
            'WCKiD',
            'Salvo',
            'Tommy Rage'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/8a83404ff5a72613c492ff9db40553c5b94eea62?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 51,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02485d79b68b82c074360fceb3',
            'width': 300
        }
    },
    {
        'name': 'Hall Of Fame',
        'artists': [
            'PHARAØH',
            'EQRIC',
            'Clayton Jones'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/0686789d26ed734fa5fbb1dd7ca4e50f9c9c0265?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 47,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e026f22977caaf4abe337231ed7',
            'width': 300
        }
    },
    {
        'name': 'Fire (with Elderbrook)',
        'artists': [
            'Ytram',
            'Elderbrook',
            'Martin Garrix'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/a369596dd69d9060f8f36747a28facb6d7b1d517?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 58,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02572839afd7741e53f9d93243',
            'width': 300
        }
    },
    {
        'name': 'Paralax',
        'artists': [
            'Aryue'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/699ce29b2d2796b56cf2da4e845abf90a16069d5?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 36,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0228869673ac6784a0fc60ddb5',
            'width': 300
        }
    },
    {
        'name': 'All My Heroes - Curbi Remix',
        'artists': [
            'Naeleck',
            'Sarah Rebecca',
            'Curbi'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/68ff0893a07ab48c398111c0b6d0919c2addfe61?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 60,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e021d06216ffc858eae6c874c21',
            'width': 300
        }
    },
    {
        'name': 'Gabber! At The Disco',
        'artists': [
            'Rawtek',
            'Sihk'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/666bf9124383be96a833f66f32c9d52778c013a5?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 35,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02beba30de197d01df216dd8cc',
            'width': 300
        }
    },
    {
        'name': 'Noise Heaven',
        'artists': [
            'Dada Life'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/9e0ecc01056b908e655c006a8d37daebc371c653?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 35,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02b72b723184264a3774b516f3',
            'width': 300
        }
    },
    {
        'name': 'Back It Up',
        'artists': [
            'The FifthGuys',
            'Coffeeshop',
            'Blvkstn'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/f89c369fe937db2484809fd6208fbdefb4cbce53?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 43,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e0221eeda37f28af950831334bf',
            'width': 300
        }
    },
    {
        'name': 'Disease - KATFYR "Tokyo Bound" Remix',
        'artists': [
            'Naeleck',
            'Oddity'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/2fcc3b69f4b122580d971847662fa7a3039ed844?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 56,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e029fe0f66272e3abc32a35770d',
            'width': 300
        }
    },
    {
        'name': 'Holler',
        'artists': [
            'ASCO',
            'FWN'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/97dfac40fde8953f1eee95983812e3804541ae93?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 35,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e027128b1cabae921169fa61826',
            'width': 300
        }
    },
    {
        'name': 'The Vibe',
        'artists': [
            'CAMIC'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/7f2b2fcbf7df2b083937c3788f6639850a8de62c?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 28,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e022544dadea57ebf42726a58ac',
            'width': 300
        }
    },
    {
        'name': 'Electronic Circus Weapon',
        'artists': [
            'Dada Life'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/c521302dc1a481c1c8c64c85f9fd25cf465c2523?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 45,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02cb686ab9a9872ae692fe06d8',
            'width': 300
        }
    },
    {
        'name': 'Face Me',
        'artists': [
            'Biometrix',
            "Rhi'N'B"
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/271d111ca084a526a8c0848e1d2dea85d7b68571?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 46,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02500a52f8a737235db59d24e2',
            'width': 300
        }
    },
    {
        'name': 'We House You',
        'artists': [
            'Kura',
            'VINNE'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/66de7063db59cfaeca434b174f83fe36b88dfc03?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 41,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02b78b44a4afdacfbd0534b2cb',
            'width': 300
        }
    },
    {
        'name': 'Readymade Sweat',
        'artists': [
            'Dada Life'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/890eb94cd2029df9b344c71afc62d251ef016861?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 48,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ee08b190281a4f655a8f26b8',
            'width': 300
        }
    },
    {
        'name': 'TEKK',
        'artists': [
            'ETC!ETC!'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/a83f259bfb019c50333ff6387b4b12926959c387?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 26,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02ef23e701875a84c9b043e19c',
            'width': 300
        }
    },
    {
        'name': 'Get Away (feat. Rama Duke)',
        'artists': [
            'Breathe Carolina',
            'Asketa & Natan Chaim',
            'Rama Duke'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/ae8fe47994406768c0d1561aee14502c85a4ac7f?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 52,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02bb9590551a9afb1d95b58f82',
            'width': 300
        }
    },
    {
        'name': 'Pathway',
        'artists': [
            'NIIKO X SWAE'
        ],
        'preview_url': 'https://p.scdn.co/mp3-preview/6c1b6244fb0e5c2d8ae95cfdbfd448c6c83d8024?cid=774b29d4f13844c495f206cafdad9c86',
        'popularity': 39,
        'image_url': {
            'height': 300,
            'url': 'https://i.scdn.co/image/ab67616d00001e02c20d2e92732bb6db2e1c25f1',
            'width': 300
        }
    }
]
