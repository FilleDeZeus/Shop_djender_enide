import random
import os
from decimal import Decimal
from django_seed import Seed
from faker import Faker
from .models import Categorie, Genre, Marque, Image, Size, Color, Shoe, Modele, Prix, ColorShoe, ColorShoeSize

fake = Faker()

data = [
    {
        'genres': [
            {
                'name':'Kid',
                'categories': [
                        {
                            'name':'Baskets',
                            'marques': [
                                {
                                    'name': 'Adidas',
                                    'modeles': [
                                        {
                                            'name': 'Stan Smith',
                                            'prix': 99.99,
                                            'images': [
                                                'stan-smith-1.png',
                                                'stan-smith-2.png',
                                                'stan-smith-3.png',
                                                'stan-smith-4.png',
                                                'stan-smith-5,png.avif',
                                            ],
                                            'colors': [
                                                {
                                                    'name': 'Black'
                                                },
                                                {
                                                    'name': 'White'
                                                }
                                            ]
                                        },
                                        {
                                                    'name': 'Superstar',
                                                    'prix': 89.99,
                                                    'images': [
                                                        'superstar-1.png',
                                                        'superstar-2.png',
                                                        'superstar-3.png',
                                                        'superstar-4.png',
                                                        'superstar-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                    ]
                                },
                                {
                                    'name': 'Nike',
                                    'modeles': [
                                        {
                                                    'name': 'Air Force',
                                                    'prix': 109.99,
                                                    'images': [
                                                        'air-force-1.png',
                                                        'air-force-2.png',
                                                        'air-force-3.png',
                                                        'air-force-4.png',
                                                        'air-force-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                        {
                                                    'name': 'Air Jordan',
                                                    'prix': 119.99,
                                                    'images': [
                                                        'air-jordan-1.png',
                                                        'air-jordan-2.png',
                                                        'air-jordan-3.png',
                                                        'air-jordan-4.png',
                                                        'air-jordan-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            'name': 'Bottes',
                            'marques': [
                                {
                                    'name': 'Moonboot',
                                    'modeles': [
                                        {
                                                    'name':'Moon Boot bottine',
                                                    'prix': 79.99,
                                                    'images': [
                                                        'basse-1.png',
                                                        'basse-2.png',
                                                        'basse-3.png',
                                                        'basse-4.png',
                                                        'basse-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                        {
                                                    'name': 'Moon Boot original',
                                                    'prix': 89.99,
                                                    'images': [
                                                        'haute-1.png',
                                                        'haute-2.png',
                                                        'haute-3.png',
                                                        'haute-4.png',
                                                        'haute-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        }
                                    ]
                                },
                                {
                                    'name': 'Ugg',
                                    'modeles': [
                                        {
                                                    'name': 'Clear mini',
                                                    'prix': 109.99,
                                                    'images': [
                                                        'basse-1.png',
                                                        'basse-2.png',
                                                        'basse-3.png',
                                                        'basse-4.png',
                                                        'basse-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                        {
                                                    'name': 'Ugg Original',
                                                    'prix': 119.99,
                                                    'images': [
                                                        'haute-1.png',
                                                        'haute-2.png',
                                                        'haute-3.png',
                                                        'haute-4.png',
                                                        'haute-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Chaussons',
                            'marques': [
                                {
                                    'name': 'Crocs',
                                    'modeles': [
                                        {
                                                    'name': 'Crocs Classic',
                                                    'prix': 39.99,
                                                    'images': [
                                                        'classic-1.png',
                                                        'classic-2.png',
                                                        'classic-3.png',
                                                        'classic-4.png',
                                                        'classic-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                        {
                                                    'name': 'Crocs fourrée',
                                                    'prix': 49.99,
                                                    'images': [
                                                        'fourree-1.png',
                                                        'fourree-2.png',
                                                        'fourree-3.png',
                                                        'fourree-4.png',
                                                        'fourree-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        }
                                    ]
                                },
                                {
                                    'name': 'Giesswein',
                                    'modeles': [
                                        {
                                                    'name': 'Oberstaufen',
                                                    'prix': 42.95,
                                                    'images': [
                                                        'laine-1.png',
                                                        'laine-2.png',
                                                        'laine-3.png',
                                                        'laine-4.png',
                                                        'laine-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Blue'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                        },
                                        {
                                                    'name': 'Strass Slim',
                                                    'prix': 42.95,
                                                    'images': [
                                                        'coton-1.png',
                                                        'coton-2.png',
                                                        'coton-3.png',
                                                        'coton-4.png',
                                                        'coton-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Pink'
                                                        },
                                                        {
                                                            'name': 'Blue'
                                                        }
                                                    ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Sandales',
                            'marques': [
                                {
                                    'name': 'Birkenstock',
                                    'modeles': [
                                        {
                                            'name': 'Birkenstock Arizona',
                                            'prix': 59.99,
                                            'images': [
                                                'sandale-1.png',
                                                'sandale-2.png',
                                                'sandale-3.png',
                                                'sandale-4.png',
                                                'sandale-5.png',
                                            ],
                                            'colors': [
                                                {
                                                    'name': 'Black'
                                                },
                                                {
                                                    'name': 'White'
                                                }
                                            ]
                                        },
                                        {
                                            'name': 'Alamo',
                                            'prix': 49.99,
                                            'images': [
                                                'tong-1.png',
                                                'tong-2.png',
                                                'tong-3.png',
                                                'tong-4.png',
                                                'tong-5.png',
                                            ],
                                            'colors': [
                                                {
                                                    'name': 'Black'
                                                },
                                                {
                                                    'name': 'White'
                                            }
                                        ]
                                },
                                    ]
                                },
                                {
                                    'name': 'Havaianas',
                                    'modeles': [
                                        {
                                                    'name': 'Marvel',
                                                    'prix': 29.99,
                                                    'images': [
                                                        'sandale-1.png',
                                                        'sandale-2.png',
                                                        'sandale-3.png',
                                                        'sandale-4.png',
                                                        'sandale-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'Blue'
                                                        }
                                                    ]
                                        },
                                        {
                                         
                                                    'name': 'Heroes',
                                                    'prix': 24.99,
                                                    'images': [
                                                        'tong-1.png',
                                                        'tong-2.png',
                                                        'tong-3.png',
                                                        'tong-4.png',
                                                        'tong-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                            
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Scratchs',
                            'marques': [
                                {
                                    'name': 'Louboutin',
                                    'modeles': [
                                        {
                                                    'name': 'Louboutin Basket',
                                                    'prix': 499.99,
                                                    'images': [
                                                        'basket-5.png',
                                                        'basket-1.png',
                                                        'basket-2.png',
                                                        'basket-3.png',
                                                        'basket-4.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Red'
                                                        },
                                                        {
                                                            'name': 'White'
                                                        }
                                                    ]
                                            
                                        },
                                        {
                                                    'name': 'Toy Toy',
                                                    'prix': 299.99,
                                                    'images': [
                                                        'sock-1.png',
                                                        'sock-2.png',
                                                        'sock-3.png',
                                                        'sock-4.png',
                                                        'sock-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Black'
                                                        },
                                                        {
                                                            'name': 'Red'
                                                        }
                                                    ]
                                            
                                        }
                                    ]
                                },
                                {
                                    'name': 'Geox',
                                    'modeles': [
                                        {
                                                    'name': 'Trottola',
                                                    'prix': 39.90,
                                                    'images': [
                                                        'basse-5.png',
                                                        'basse-1.png',
                                                        'basse-2.png',
                                                        'basse-3.png',
                                                        'basse-4.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Camel'
                                                        },
                                                        {
                                                            'name': 'Blue'
                                                        }
                                                    ]
                                            
                                        },
                                        {
                                                    'name': 'Grayjay Junior',
                                                    'prix': 79.00,
                                                    'images': [
                                                        'montante-1.png',
                                                        'montante-2.png',
                                                        'montante-3.png',
                                                        'montante-4.png',
                                                        'montante-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Blue'
                                                        },
                                                        {
                                                            'name': 'Black'
                                                        }
                                                    ]
                                            
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            'name': 'Sport',
                            'marques': [
                                {
                                    'name': 'Artengo',
                                    'modeles': [
                                        {
                                          
                                                    'name': 'Fast Kd Scratch',
                                                    'prix': 30.00,
                                                    'images': [
                                                        'scratch-1.png',
                                                        'scratch-2.png',
                                                        'scratch-3.png',
                                                        'scratch-4.png',
                                                        'scratch-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Pink'
                                                        },
                                                        {
                                                            'name': 'Yellow'
                                                        }
                                                    ]
                                            
                                        },
                                        {
                                            'name': 'Lacet',
                                            'shoes': [
                                                {
                                                    'name': 'Fasr Jr Lacet',
                                                    'prix': 149.99,
                                                    'images': [
                                                        'Lacet-1.png',
                                                        'Lacet-2.png',
                                                        'Lacet-3.png',
                                                        'Lacet-4.png',
                                                        'Lacet-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Blue'
                                                        },
                                                        {
                                                            'name': 'Red'
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                    ]
                                },
                                {
                                    'name': 'Quechua',
                                    'modeles': [
                                        {
                                            'name': 'Scratch',
                                            'shoes': [
                                                {
                                                    'name': 'Warm Scratch',
                                                    'prix': 119.99,
                                                    'images': [
                                                        'scratch-1.png',
                                                        'scratch-2.png',
                                                        'scratch-3.png',
                                                        'scratch-4.png',
                                                        'scratch-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Purple'
                                                        },
                                                        {
                                                            'name': 'Black'
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            'name': 'Lacet',
                                            'shoes': [
                                                {
                                                    'name': 'Crossrock',
                                                    'prix': 139.99,
                                                    'images': [
                                                        'lacet-1.png',
                                                        'lacet-2.png',
                                                        'lacet-3.png',
                                                        'lacet-4.png',
                                                        'lacet-5.png',
                                                    ],
                                                    'colors': [
                                                        {
                                                            'name': 'Green'
                                                        },
                                                        {
                                                            'name': 'Blue'
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
            },
            {
                'name': 'Men',
                'categories': [
                    {
                        'name': 'Baskets',
                        'marques': [
                            {
                                'name': 'Adidas',
                                'modeles': [
                                    {
                                        'name': 'Stan-smith',
                                        'shoes': [
                                            {
                                                'name': 'Stan Smith',
                                                'prix': 99.99,
                                                'images': [
                                                    'stan-smith-1.png',
                                                    'stan-smith-2.png',
                                                    'stan-smith-3.png',
                                                    'stan-smith-4.png',
                                                    'stan-smith-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Superstar',
                                        'shoes': [
                                            {
                                                'name': 'Superstar',
                                                'prix': 129.99,
                                                'images': [
                                                    'superstar-1.png',
                                                    'superstar-2.png',
                                                    'superstar-3.png',
                                                    'superstar-4.png',
                                                    'superstar-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }   
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Nike',
                                'modeles': [
                                    {
                                        'name': 'Air-force',
                                        'shoes': [
                                            {
                                                'name': 'Air Force',
                                                'prix': 149.99,
                                                'images': [
                                                    'air-force-1.png',
                                                    'air-force-2.png',
                                                    'air-force-3.png',
                                                    'air-force-4.png',
                                                    'air-force-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        'name': 'Air-jordan',
                                        'shoes': [
                                            {
                                                'name': 'Air Jordan',
                                                'prix': 199.99,
                                                'images': [
                                                    'air-jordan-1.png',
                                                    'air-jordan-2.png',
                                                    'air-jordan-3.png',
                                                    'air-jordan-4.png',
                                                    'air-jordan-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        'name': 'Bottes',
                        'marques': [
                            {
                                'name': 'Moonboot',
                                'modeles': [
                                    {
                                        'name': 'Basse',
                                        'shoes': [
                                            {
                                                'name': 'Moon Boot bottine',
                                                'prix': 79.99,
                                                'images': [
                                                    'basse-1.png',
                                                    'basse-2.png',
                                                    'basse-3.png',
                                                    'basse-4.png',
                                                    'basse-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                        
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        'name': 'Haute',
                                        'shoes': [
                                            {
                                                'name': 'Moon Boot original',
                                                'prix': 99.99,
                                                'images': [
                                                    'haute-1.png',
                                                    'haute-2.png',
                                                    'haute-3.png',
                                                    'haute-4.png',
                                                    'haute-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Ugg',
                                'modeles': [
                                    {
                                        'name': 'Basse',
                                        'shoes': [
                                            {
                                                'name': 'Clear mini',
                                                'prix': 129.99,
                                                'images': [
                                                    'basse-1.png',
                                                    'basse-2.png',
                                                    'basse-3.png',
                                                    'basse-4.png',
                                                    'basse-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Haute',
                                        'shoes': [
                                            {
                                                'name': 'Ugg Original',
                                                'prix': 149.99,
                                                'images': [
                                                    'haute-1.png',
                                                    'haute-2.png',
                                                    'haute-3.png',
                                                    'haute-4.png',
                                                    'haute-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Chaussons',
                        'marques': [
                            {
                                'name': 'Crocs',
                                'modeles': [
                                    {
                                        'name': 'Classic',
                                        'shoes': [
                                            {
                                                'name': 'Crocs Classic',
                                                'prix': 29.99,
                                                'images': [
                                                    'classic-1.png',
                                                    'classic-2.png',
                                                    'classic-3.png',
                                                    'classic-4.png',
                                                    'classic-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Fourree',
                                        'shoes': [
                                            {
                                                'name': 'Crocs fourrée',
                                                'prix': 39.99,
                                                'images': [
                                                    'fourree-1.png',
                                                    'fourree-2.png',
                                                    'fourree-3.png',
                                                    'fourree-4.png',
                                                    'fourree-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Giesswein',
                                'modeles': [
                                    {
                                        'name': 'Laine',
                                        'shoes': [
                                            {
                                                'name': 'Wildpoldsried',
                                                'prix': 69.95,
                                                'images': [
                                                    'laine-1.png',
                                                    'laine-2.png',
                                                    'laine-3.png',
                                                    'laine-4.png',
                                                    'laine-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'Camel'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Coton',
                                        'shoes': [
                                            {
                                                'name': 'Berlin',
                                                'prix': 59.95,
                                                'images': [
                                                    'coton-1.png',
                                                    'coton-2.png',
                                                    'coton-3.png',
                                                    'coton-4.png',
                                                    'coton-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Grey'
                                                    },
                                                    {
                                                        'name': 'Blue'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        'name': 'Mocassins',
                        'marques': [
                            {
                                'name': 'Louboutin',
                                'modeles': [
                                    {
                                        'name': 'Cuir',
                                        'shoes': [
                                            {
                                                'name': 'Néo romantique',
                                                'prix': 499.99,
                                                'images': [
                                                    'cuir-1.png',
                                                    'cuir-2.png',
                                                    'cuir-3.png',
                                                    'cuir-4.png',
                                                    'cuir-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        'name': 'Velours',
                                        'shoes': [
                                            {
                                                'name': 'Equiswing',
                                                'prix': 599.99,
                                                'images': [
                                                    'velours-1.png',
                                                    'velours-2.png',
                                                    'velours-3.png',
                                                    'velours-4.png',
                                                    'velours-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                'name': 'Scarosso',
                                'modeles': [
                                    {
                                        'name': 'Cuir',
                                        'shoes': [
                                            {
                                                'name': 'Marzio ',
                                                'prix': 399.99,
                                                'images': [
                                                    'cuir-1.png',
                                                    'cuir-2.png',
                                                    'cuir-3.png',
                                                    'cuir-4.png',
                                                    'cuir-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        'name': 'Velours',
                                        'shoes': [
                                            {
                                                'name': 'George',
                                                'prix': 499.99,
                                                'images': [
                                                    'velours-1.png',
                                                    'velours-2.png',
                                                    'velours-3.png',
                                                    'velours-4.png',
                                                    'velours-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Sandales',
                        'marques': [
                            {
                                'name': 'Birkenstock',
                                'modeles': [
                                    {
                                        'name': 'Sandale',
                                        'shoes': [
                                            {
                                                'name': 'Arizona',
                                                'prix': 79.99,
                                                'images': [
                                                    'sandale-1.png',
                                                    'sandale-2.png',
                                                    'sandale-3.png',
                                                    'sandale-4.png',
                                                    'sandale-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Tong',
                                        'shoes': [
                                            {
                                                'name': 'Alamo',
                                                'prix': 49.99,
                                                'images': [
                                                    'tong-1.png',
                                                    'tong-2.png',
                                                    'tong-3.png',
                                                    'tong-4.png',
                                                    'tong-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Havaianas',
                                'modeles': [
                                    {
                                        'name': 'Sandale',
                                        'shoes': [
                                            {
                                                'name': 'Slide Classic',
                                                'prix': 39.99,
                                                'images': [
                                                    'sandale-1.png',
                                                    'sandale-2.png',
                                                    'sandale-3.png',
                                                    'sandale-4.png',
                                                    'sandale-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Tong',
                                        'shoes': [
                                            {
                                                'name': 'Havainas original',
                                                'prix': 29.99,
                                                'images': [
                                                    'tong-1.png',
                                                    'tong-2.png',
                                                    'tong-3.png',
                                                    'tong-4.png',
                                                    'tong-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Sport',
                        'marques': [
                            {
                                'name': 'Quechua',
                                'modeles': [
                                    {
                                        'name': 'Running',
                                        'shoes': [
                                            {
                                                'name': 'Fresh',
                                                'prix': 69.99,
                                                'images': [
                                                    'running-1.png',
                                                    'running-2.png',
                                                    'running-3.png',
                                                    'running-4.png',
                                                    'running-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Grey'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Randonnee',
                                        'shoes': [
                                            {
                                                'name': 'Ultra Warm',
                                                'prix': 119.99,
                                                'images': [
                                                    'randonnee-1.png',
                                                    'randonnee-2.png',
                                                    'randonnee-3.png',
                                                    'randonnee-4.png',
                                                    'randonnee-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'Blue'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                'name': 'Salomon',
                                'modeles': [
                                    {
                                        'name': 'Running',
                                        'shoes': [
                                            {
                                                'name': 'Run speedcross',
                                                'prix': 109.99,
                                                'images': [
                                                    'running-1.png',
                                                    'running-2.png',
                                                    'running-3.png',
                                                    'running-4.png',
                                                    'running-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Blue'
                                                    },
                                                    {
                                                        'name': 'Orange'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Randonnee',
                                        'shoes': [
                                            {
                                                'name': 'Rando cross',
                                                'prix': 89.99,
                                                'images': [
                                                    'randonnee-1.png',
                                                    'randonnee-2.png',
                                                    'randonnee-3.png',
                                                    'randonnee-4.png',
                                                    'randonnee-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Grey'
                                                    },
                                                    {
                                                        'name': 'Green'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                ]
            },
            {
                'name': 'Women',
                'categories':[
                    {
                        'name':'Baskets',
                        'marques': [
                            {
                                'name': 'Adidas',
                                'modeles': [
                                    {
                                        'name': 'Stan-smith',
                                        'shoes': [
                                            {
                                                'name': 'Stan Smith',
                                                'prix': 99.99,
                                                'images': [
                                                    'stan-smith-1.png',
                                                    'stan-smith-2.png',
                                                    'stan-smith-3.png',
                                                    'stan-smith-4.png',
                                                    'stan-smith-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Superstar',
                                        'shoes': [
                                            {
                                                'name': 'Superstar',
                                                'prix': 129.99,
                                                'images': [
                                                    'superstar-1.png',
                                                    'superstar-2.png',
                                                    'superstar-3.png',
                                                    'superstar-4.png',
                                                    'superstar-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                'name': 'Nike',
                                'modeles': [
                                    {
                                        'name': 'Air-force',
                                        'shoes': [
                                            {
                                                'name': 'Air Force',
                                                'prix': 149.99,
                                                'images': [
                                                    'air-force-1.png',
                                                    'air-force-2.png',
                                                    'air-force-3.png',
                                                    'air-force-4.png',
                                                    'air-force-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        'name': 'Air-jordan',
                                        'shoes': [
                                            {
                                                'name': 'Air Jordan',
                                                'prix': 199.99,
                                                'images': [
                                                    'air-jordan-1.png',
                                                    'air-jordan-2.png',
                                                    'air-jordan-3.png',
                                                    'air-jordan-4.png',
                                                    'air-jordan-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Bottes',
                        'marques': [
                            {
                                'name': 'Moonboot',
                                'modeles': [
                                    {
                                        'name': 'Basse',
                                        'shoes': [
                                            {
                                                'name': 'Moon Boot bottine',
                                                'prix': 79.99,
                                                'images': [
                                                    'basse-1.png',
                                                    'basse-2.png',
                                                    'basse-3.png',
                                                    'basse-4.png',
                                                    'basse-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Haute',
                                        'shoes': [
                                            {
                                                'name': 'Moon Boot Original',
                                                'prix': 99.99,
                                                'images': [
                                                    'haute-1.png',
                                                    'haute-2.png',
                                                    'haute-3.png',
                                                    'haute-4.png',
                                                    'haute-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Ugg',
                                'modeles': [
                                    {
                                        'name': 'Basse',
                                        'shoes': [
                                            {
                                                'name': 'Clear mini',
                                                'prix': 129.99,
                                                'images': [
                                                    'basse-1.png',
                                                    'basse-2.png',
                                                    'basse-3.png',
                                                    'basse-4.png',
                                                    'basse-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Haute',
                                        'shoes': [
                                            {
                                                'name': 'Ugg Original',
                                                'prix': 149.99,
                                                'images': [
                                                    'haute-1.png',
                                                    'haute-2.png',
                                                    'haute-3.png',
                                                    'haute-4.png',
                                                    'haute-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Chaussons',
                        'marques': [
                            {
                                'name': 'Crocs',
                                'modeles': [
                                    {
                                        'name': 'Classic',
                                        'shoes': [
                                            {
                                                'name': 'Crocs Classic ',
                                                'prix': 29.99,
                                                'images': [
                                                    'classic-1.png',
                                                    'classic-2.png',
                                                    'classic-3.png',
                                                    'classic-4.png',
                                                    'classic-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Fourree',
                                        'shoes': [
                                            {
                                                'name': 'Crocs fourrée',
                                                'prix': 39.99,
                                                'images': [
                                                    'fourree-1.png',
                                                    'fourree-2.png',
                                                    'fourree-3.png',
                                                    'fourree-4.png',
                                                    'fourree-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Giesswein',
                                'modeles': [
                                    {
                                        'name': 'Laine',
                                        'shoes': [
                                            {
                                                'name': 'Hohenau ',
                                                'prix': 69.95,
                                                'images': [
                                                    'laine-1.png',
                                                    'laine-2.png',
                                                    'laine-3.png',
                                                    'laine-4.png',
                                                    'laine-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'Grey'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Coton',
                                        'shoes': [
                                            {
                                                'name': 'Dohel',
                                                'prix': 79.49,
                                                'images': [
                                                    'coton-1.png',
                                                    'coton-2.png',
                                                    'coton-3.png',
                                                    'coton-4.png',
                                                    'coton-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Blue'
                                                    },
                                                    {
                                                        'name': 'Grey'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        'name': 'Souliers',
                        'marques': [
                            {
                                'name': 'Louboutin',
                                'modeles': [
                                    {
                                        'name': 'Plat',
                                        'shoes': [
                                            {
                                                'name': 'Mules',
                                                'prix': 499.99,
                                                'images': [
                                                    'plat-1.png',
                                                    'plat-2.png',
                                                    'plat-3.png',
                                                    'plat-4.png',
                                                    'plat-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Plateforme',
                                        'shoes': [
                                            {
                                                'name': 'Superaclou',
                                                'prix': 599.99,
                                                'images': [
                                                    'plateforme-1.png',
                                                    'plateforme-2.png',
                                                    'plateforme-3.png',
                                                    'plateforme-4.png',
                                                    'plateforme-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Scarosso',
                                'modeles': [
                                    {
                                        'name': 'Cuir',
                                        'shoes': [
                                            {
                                                'name': 'Harper',
                                                'prix': 399.99,
                                                'images': [
                                                    'cuir-1.png',
                                                    'cuir-2.png',
                                                    'cuir-3.png',
                                                    'cuir-4.png',
                                                    'cuir-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]   
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Velours',
                                        'shoes': [
                                            {
                                                'name': 'Ludovica',
                                                'prix': 499.99,
                                                'images': [
                                                    'velours-1.png',
                                                    'velours-2.png',
                                                    'velours-3.png',
                                                    'velours-4.png',
                                                    'velours-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White',
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Sandales',
                        'marques': [
                            {
                                'name': 'Birkenstock',
                                'modeles': [
                                    {
                                        'name': 'Sandale',
                                        'shoes': [
                                            {
                                                'name': 'Arizona',
                                                'prix': 79.99,
                                                'images': [
                                                    'sandale-1.png',
                                                    'sandale-2.png',
                                                    'sandale-3.png',
                                                    'sandale-4.png',
                                                    'sandale-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Tong',
                                        'shoes': [
                                            {
                                                'name': 'Alamo',
                                                'prix': 49.99,
                                                'images': [
                                                    'tong-1.png',
                                                    'tong-2.png',
                                                    'tong-3.png',
                                                    'tong-4.png',
                                                    'tong-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                        
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                'name': 'Havaianas',
                                'modeles': [
                                    {
                                        'name': 'Sandale',
                                        'shoes': [
                                            {
                                                'name': 'Slide Classic',
                                                'prix': 39.99,
                                                'images': [
                                                    'sandale-1.png',
                                                    'sandale-2.png',
                                                    'sandale-3.png',
                                                    'sandale-4.png',
                                                    'sandale-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White',
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Tong',
                                        'shoes': [
                                            {
                                                'name': 'Havainas original',
                                                'prix': 29.99,
                                                'images': [
                                                    'tong-1.png',
                                                    'tong-2.png',
                                                    'tong-3.png',
                                                    'tong-4.png',
                                                    'tong-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Black'
                                                    },
                                                    {
                                                        'name': 'White'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Sport',
                        'marques': [
                            {
                                'name': 'Quechua',
                                'modeles': [
                                    {
                                        'name': 'Running',
                                        'shoes': [
                                            {
                                                'name': 'Run Active',
                                                'prix': 129.99,
                                                'images': [
                                                    'running-1.png',
                                                    'running-2.png',
                                                    'running-3.png',
                                                    'running-4.png',
                                                    'running-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Blue'
                                                    },
                                                    {
                                                        'name': 'Pink'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Randonnee',
                                        'shoes': [
                                            {
                                                'name': 'Rando Fresh',
                                                'prix': 149.99,
                                                'images': [
                                                    'randonnee-1.png',
                                                    'randonnee-2.png',
                                                    'randonnee-3.png',
                                                    'randonnee-4.png',
                                                    'randonnee-5.png',
                                                ],
                                                'colors': [
                                                    {
                                                        'name': 'Blue'
                                                    },
                                                    {
                                                        'name': 'Pink'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Salomon',
                                'modeles': [
                                    {
                                        'name': 'Running',
                                        'shoes': [
                                            {
                                                'name': 'Speedcross',
                                                'prix': 109.99,
                                                'images': [
                                                            'running-1.png',
                                                            'running-2.png',
                                                            'running-3.png',
                                                            'running-4.png',
                                                            'running-5.png',
                                                        ],
                                                'colors': [
                                                    {
                                                        'name': 'Purple',
                                                    },
                                                    {
                                                        'name': 'White',
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Randonnee',
                                        'shoes': [
                                            {
                                                'name': 'Rando Fresh',
                                                'prix': 129.99,
                                                'images': [
                                                            'randonnee-1.png',
                                                            'randonnee-2.png',
                                                            'randonnee-3.png',
                                                            'randonnee-4.png',
                                                            'randonnee-5.png',
                                                        ],
                                                'colors': [
                                                    {
                                                        'name': 'Black',
                                                    },
                                                    {
                                                        'name': 'Blue',
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                ]
            }
        ]
    }
]


def seed_data():
   
    # Parcourir les genres
    for genre_data in data[0]['genres']:
        genre_name = genre_data['name']
        genre, _ = Genre.objects.get_or_create(name=genre_name)

        
        for categorie_data in genre_data['categories']:
            categorie_name = categorie_data['name']
            categorie, _ = Categorie.objects.get_or_create(name=categorie_name)
            categorie.genre.add(genre)
            
            for marque_data in categorie_data['marques']:
                marque_name = marque_data['name']
                marque_logo = os.path.join('logo', f"{marque_name.lower().replace(' ', '')}.png")
                marque, _ = Marque.objects.get_or_create(name=marque_name, logo=marque_logo, categorie=categorie)
                
                for modele_data in marque_data['modeles']:
                    modele_name = modele_data['name']
                    modele, _ = Modele.objects.get_or_create(name=modele_name, marque=marque)
                    
                    for shoe_data in modele_data['shoes']:
                        shoe_name = shoe_data['name']
                        country = fake.country()[:50]
                        material = fake.word()
                        shipping = random.choice(['Free Shipping', 'Express Shipping'])
                        description = fake.text(max_nb_chars=300)
                        shoe,_= Shoe.objects.get_or_create(name=shoe_name, country=country, material=material, shipping=shipping, description=description, modele=modele, categorie=categorie)

                        # Gestion du prix unique
                        prix_data = shoe_data['prix']
                        prix_value = '{:.2f}'.format(prix_data)

                        promotion = random.randrange(0, 60, 5)
                        prix_promo = '{:.2f}'.format(prix_data - (prix_data * promotion / 100))
                        prix, _ = Prix.objects.get_or_create(prix=prix_value,promotion=promotion, prix_promo=prix_promo , shoe=shoe)
                        
                        
                        for color_data in shoe_data['colors']:
                            color_name = color_data['name']
                            images_data = shoe_data['images']
                            color, _ = Color.objects.get_or_create(name=color_name)
                            color.shoe.add(shoe)

                            
                            
                #             # Générer les tailles et les stocks pour chaque chaussure
                #             # Définir la liste de tailles en fonction du genre
                            kid_size_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
                            women_size_list = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
                            men_size_list = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    
                            if genre_name == 'Kid':
                                size_list = kid_size_list
                            elif genre_name == 'Women':
                                size_list = women_size_list
                            elif genre_name == 'Men':
                                size_list = men_size_list
                                
                            # Créer une instance de ColorShoe avec la couleur et la chaussure correspondantes
                            colorshoe, _ = ColorShoe.objects.get_or_create(color=color, shoe=shoe)

                            image = Image.objects.create(
                                image_1=os.path.join( 'shoes', genre_name, categorie_name, marque_name, modele_name, color_name, images_data[0]),
                                image_2=os.path.join( 'shoes', genre_name, categorie_name, marque_name, modele_name, color_name, images_data[1]),
                                image_3=os.path.join( 'shoes', genre_name, categorie_name, marque_name, modele_name, color_name, images_data[2]),
                                image_4=os.path.join( 'shoes', genre_name, categorie_name, marque_name, modele_name, color_name, images_data[3]),
                                image_5=os.path.join( 'shoes', genre_name, categorie_name, marque_name, modele_name, color_name, images_data[4]),
                                colorshoe=colorshoe
                            )
                            # Récupérer la liste des tailles pour cette couleur
                            # size_list = color_data['sizes']

                            for size_value in size_list:
                                # Récupérer ou créer une instance de Size pour cette taille
                                size, _ = Size.objects.get_or_create(size=size_value)

                                # Associer la taille à l'instance de ColorShoe en utilisant la relation sizes
                                colorshoe.sizes.add(size)

                                # Créer une instance de ColorShoeSize pour associer la taille à la combinaison de couleur de chaussure
                                stock = random.randint(0, 3)  # Générer le stock aléatoire entre 0 et 15
                                colorshoesize, _ = ColorShoeSize.objects.get_or_create(colorshoe=colorshoe, size=size, stock=stock)